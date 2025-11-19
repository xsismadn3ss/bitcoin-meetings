import flet as ft
from ._layout_view import LayoutNavBar


class ProfileView(LayoutNavBar):
    def __init__(self, page: ft.Page, route: str = "/profile"):
        super().__init__(
            page=page,
            route=route,
            controls=[
                ft.Column(
                    [ft.Text("Perfil", size=28, weight=ft.FontWeight.BOLD)],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
        )
