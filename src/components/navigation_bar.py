import flet as ft
from models.route import Route


class NavBar:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.routes = [Route(route="/", name="Inicio", icon=ft.Icons.HOME)]

    def build(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            selected_index=0,
            on_change=lambda e: self.page.go(
                self.routes[e.control.selected_index].route
            ),
            destinations=[
                ft.NavigationBarDestination(
                    icon=route.icon,
                    label=route.name,
                )
                for route in self.routes
            ],
        )
