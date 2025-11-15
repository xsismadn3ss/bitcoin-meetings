import flet as ft
from components.navigation_bar import NavBar


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",
            navigation_bar=NavBar(page=page).build(),
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
