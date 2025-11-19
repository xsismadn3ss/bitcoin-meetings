import json
import httpx
import flet as ft
from pydantic import ValidationError
from service.auth_service import login
from models.auth import AuthLoginDto

from ._layout_back_arrow import LayoutBackArrow
from ._layout_error_dialog import LayoutErrorDialog


class LoginView(LayoutBackArrow, LayoutErrorDialog):
    def __init__(
        self, page: ft.Page, title: str = "Inicio de sesión", route: str = "/login"
    ):
        self.email_text = ft.TextField(
            label="Email",
            value="",
            border_radius=15,
            border_color=ft.Colors.SECONDARY_CONTAINER,
            focused_border_color=ft.Colors.PRIMARY_CONTAINER,
        )
        self.password_text = ft.TextField(
            label="Contraseña",
            value="",
            password=True,
            can_reveal_password=True,
            border_radius=15,
            border_color=ft.Colors.SECONDARY_CONTAINER,
            focused_border_color=ft.Colors.PRIMARY_CONTAINER,
        )

        super().__init__(
            page,
            title,
            route,
            "/",
            controls=[
                ft.Column(
                    [
                        ft.ResponsiveRow(
                            [
                                ft.Container(
                                    self.email_text,
                                    col={"xs": 12, "md": 6, "lg": 4},
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.ResponsiveRow(
                            [
                                ft.Container(
                                    self.password_text,
                                    col={"xs": 12, "md": 6, "lg": 4},
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.ElevatedButton(
                            "Iniciar sesión",
                            icon=ft.Icons.LOGIN,
                            on_click=self._handle_login,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
        )

    async def _handle_login(self, e):

        try:
            data = AuthLoginDto(
                email=self.email_text.value, password=self.password_text.value  # type: ignore
            )
            result = await login(data)

            token = result.get("token")
            name = result.get("name")
            await self.page.client_storage.set_async("auth_token", token)  # type: ignore
            await self.page.client_storage.set_async("name", name)  # type: ignore

            self.page.update()  # type: ignore
            self.page.go("/")  # type: ignore
        except ValidationError as ve:
            errors: list[str] = []
            for error in ve.errors():
                campo = error["loc"][0]  # 'email' o 'password'
                tipo = error["type"]  # 'string_too_short', 'value_error'

                if campo == "email":
                    errors.append("Dirección de correo electrónico inválida")
                if campo == "password" and tipo == "string_too_short":
                    errors.append("La contraseña debe tener mínimo 6 carácteres")
            self.open_dialog(
                self.build_error_dialog(
                    errors,
                    title="Advertencia",
                    color=ft.Colors.ORANGE,
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.ORANGE),
                )
            )
        except httpx.HTTPStatusError as err:
            http_error: dict = json.loads(err.response.text)
            self.open_dialog(self.build_error_dialog([http_error["message"]]))
        except Exception as e:
            self.open_dialog(self.build_error_dialog([f"{str(e)}"]))
