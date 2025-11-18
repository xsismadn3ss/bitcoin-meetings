import json
import httpx
import flet as ft
from pydantic import ValidationError
from service.auth_service import login

from ._layout_view import LayoutView


class LoginView(LayoutView):
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
        self.status = ft.Text(visible=False)

        super().__init__(
            page,
            route,
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(
                                "Inicio de sesión",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                            ),
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
                        self.status,
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
        self.status.visible = True
        self.status.color = ft.Colors.WHITE
        self.status.value = "Cargando..."
        self.page.update()  # type: ignore

        try:
            result = await login(self.email_text.value, self.password_text.value)

            token = result.get("token")
            name = result.get("name")
            await self.page.client_storage.set_async("auth_token", token)  # type: ignore
            await self.page.client_storage.set_async("name", name)  # type: ignore

            self.status.value = f"Bienvenido {name}"
            self.status.color = ft.Colors.GREEN

            self.page.update()  # type: ignore
            self.page.go("/")  # type: ignore

        except ValidationError as ve:
            self.status.value = f'Datos inválidos: {ve.errors()[0]["msg"]}'
            self.status.color = ft.Colors.ORANGE
        except httpx.HTTPStatusError as err:
            error: dict = json.loads(err.response.text)
            self.status.value = f"Error: {error.get("message")}"
            self.status.color = ft.Colors.RED
        except Exception as e:
            self.status.value = f"Error inesperado: {str(e)}"
            self.status.color = ft.Colors.RED

        self.page.update()  # type: ignore
