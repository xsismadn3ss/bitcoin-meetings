import flet as ft
from .layout_view import LayoutView


class LoginView(LayoutView):
    def __init__(self, page: ft.Page, route: str = "/login"):
        super().__init__(
            page,
            route,
            controls=[
                ft.Column(
                    [ft.Text("Inicio de sesión", size=28, weight=ft.FontWeight.BOLD)]
                ),
                self._form(),
            ],
        )

    def _handle_login(self):
        # TODO: implementar inicio de sesión y hacer petición a un endpoint
        pass

    def _form(self):
        user_text = ft.TextField(label="Usuario")
        password_text = ft.TextField(
            label="Contraseña", password=True, can_reveal_password=True
        )
        login_btn = ft.ElevatedButton(
            "Iniciar sesión",
            icon=ft.Icons.LOGIN,
            on_click=lambda e: print("Implementar inicio de sesión"),
        )

        return ft.Column([user_text, password_text, login_btn])
