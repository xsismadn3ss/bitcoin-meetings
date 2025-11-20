import flet as ft
from views._layout_navbar import LayoutNavBar


class HomeView(LayoutNavBar):
    def __init__(self, page: ft.Page, route: str = "/"):
        super().__init__(
            page=page,
            route=route,
            controls=[
                ft.Column(
                    [
                        ft.Text("Inicio", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Bienvenido a Bitcoin Meetings Directory", size=14),
                    ],
                ),
            ],
        )
