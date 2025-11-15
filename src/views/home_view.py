import flet as ft
from views.layout_view import LayoutView


class HomeView(LayoutView):
    def __init__(self, page: ft.Page, route: str = "/"):
        super().__init__(
            page=page,
            route=route,
            controls=[
                ft.Column(
                    [
                        ft.Text("¡Bienvenido!", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Esta es la página principal.", size=16),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
        )
