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
                        ft.Text("Inicio", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Bienvenido a Bitcoin Meetings Directory", size=14)
                    ],
                ),
            ],
        )
