import json
import httpx
import flet as ft
from pydantic import ValidationError
from service.auth_service import register
from models.user import RegisterUserDto

from ._layout_error_dialog import LayoutErrorDialog, ErrorLevel
from ._layout_back_arrow import LayoutBackArrow


class RegisterView(LayoutBackArrow, LayoutErrorDialog):
    def __init__(
        self,
        page: ft.Page,
        title: str = "Registrar cuenta",
        route: str = "/register",
        back_route: str = "/",
        **kwargs,
    ):
        style = {"xs": 12, "md": 6, "lg": 4}

        self.name_text = ft.TextField(
            label="Nombre",
            border_radius=15,
            border_color=ft.Colors.SECONDARY_CONTAINER,
            focused_border_color=ft.Colors.PRIMARY_CONTAINER,
            on_submit=self.handle_register
        )
        self.email_text = ft.TextField(
            label="Email",
            border_radius=15,
            border_color=ft.Colors.SECONDARY_CONTAINER,
            focused_border_color=ft.Colors.PRIMARY_CONTAINER,
            on_submit=self.handle_register
        )
        self.password_text = ft.TextField(
            label="Contraseña",
            border_radius=15,
            border_color=ft.Colors.SECONDARY_CONTAINER,
            focused_border_color=ft.Colors.PRIMARY_CONTAINER,
            password=True,
            can_reveal_password=True,
            on_submit=self.handle_register
        )

        super().__init__(
            page,
            title,
            route,
            back_route,
            controls=[
                ft.Column(
                    [
                        ft.ResponsiveRow(
                            [ft.Container(self.name_text, col=style)],  # type: ignore
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.ResponsiveRow(
                            [ft.Container(self.email_text, col=style)],  # type: ignore
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.ResponsiveRow(
                            [ft.Container(self.password_text, col=style)],  # type: ignore
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.ElevatedButton(
                            "Registrarse",
                            icon=ft.Icons.SEND,
                            on_click=self.handle_register,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS,
                    height=500,
                )
            ],
            **kwargs,
        )

    async def handle_register(self, e):
        self.page.update()  # type: ignore
        try:
            data = RegisterUserDto(
                name=self.name_text.value,  # type: ignore
                email=self.email_text.value,  # type: ignore
                password=self.password_text.value,  # type: ignore
            )
            result = await register(data)

            token = result.get("token")
            name = result.get("name")
            await self.page.client_storage.set_async("auth_token", token)  # type: ignore
            await self.page.client_storage.set_async("name", name)  # type: ignore

            self.page.update()  # type: ignore
            self.page.go("/")  # type: ignore

        except ValidationError as ve:
            errors: list[str] = []
            for error in ve.errors():
                campo = error["loc"][0]

                if campo == "email":
                    errors.append("Dirección de correo electrónico inválida")
                if campo == "password":
                    errors.append(
                        "La contraseña no es segura. Debe tener al menos 8 caracteres. Debe contener números, mayúsculas y minúsculas"
                    )
                if campo == "name":
                    errors.append("El nombre no debe estar vacío")

            self.open_dialog(
                self.build_error_dialog(
                    errors,
                    "Advertencia",
                    level=ErrorLevel.WARNING,
                    height=150 if len(errors) > 2 else 75,
                )
            )
        except httpx.HTTPStatusError as err:
            http_error: dict = json.loads(err.response.text)
            self.open_dialog(self.build_error_dialog([http_error["message"]]))
        except Exception as ex:
            self.open_dialog(self.build_error_dialog([f"{str(ex)}"]))
