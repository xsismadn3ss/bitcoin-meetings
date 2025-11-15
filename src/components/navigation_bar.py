import flet as ft
from models.route import Route


class NavBar:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.routes = [
            Route("/", "Inicio", ft.Icons.HOME),
            Route("/profile", "Perfil", ft.Icons.PEOPLE),
        ]

    def build(self) -> ft.NavigationBar:
        index = self.select_button()
        return ft.NavigationBar(
            selected_index=index,
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

    def select_button(self):
        route = self.page.route
        index = None
        for i, r in enumerate(self.routes):
            if r.route != route:
                continue
            index = i
        return index
