import json
import httpx
import flet as ft
from pydantic import ValidationError
from service.auth_service import login
from models.auth import AuthLoginDto
from components.title import Title

from ._layout_view import LayoutNavBar


class LoginView(LayoutNavBar):
    def __init__(self, page: ft.Page, route: str = "/login"):
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
            route,
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            Title("Inicio de sesión"),
                            margin=ft.margin.only(bottom=15, top=15),
                        ),
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
                self._error_dialog(errors, title="Advertencia", color=ft.Colors.ORANGE)
            )
        except httpx.HTTPStatusError as err:
            http_error: dict = json.loads(err.response.text)
            self.open_dialog(self._error_dialog([http_error["message"]]))
        except Exception as e:
            self.open_dialog(self._error_dialog([f"{str(e)}"]))

    def _error_dialog(
        self,
        errors: list[str],
        title: str = "Error",
        color: ft.ColorValue | None = ft.Colors.RED,
    ):
        modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, weight=ft.FontWeight.BOLD),
            content=ft.Column(
                [
                    ft.Text(f"• {e}", color=color, weight=ft.FontWeight.W_500)
                    for e in errors
                ],
                scroll=ft.ScrollMode.ADAPTIVE,
                height=75,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                tight=True,
            ),
            actions=[
                ft.TextButton("cerrar", on_click=lambda e: self.close_dialog(modal))  # type: ignore
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        return modal
