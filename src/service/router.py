import flet as ft
from typing import Dict, Callable

# vistas
from views.home_view import HomeView
from views.profile_view import ProfileView


class Router:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page = page
        self.routes: Dict[str, Callable[[ft.Page], ft.View]] = {
            "/": lambda p: HomeView(p),
            "/profile": lambda p: ProfileView(p),
        }

    def route_change(self, route):
        # Limpiar todas las vistas anteriores
        self.page.views.clear()

        # Obtener la vista correspondiente a la ruta actual
        view_factory = self.routes.get(self.page.route)
        if view_factory:
            view = view_factory(self.page)
            self.page.views.append(view)
        else:
            # Vista 404 si no existe la ruta
            self.page.views.append(
                ft.View(
                    route=self.page.route,
                    controls=[
                        ft.AppBar(title=ft.Text("Error 404")),
                        ft.Text("Página no encontrada", size=24),
                        ft.ElevatedButton(
                            "Ir a Inicio", on_click=lambda _: self.page.go("/")
                        ),
                    ],
                )
            )

        self.page.update()

    def view_pop(self, view):
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            route = getattr(top_view, "route", None)
            if route is None:
                route = "/"  # todo: implementar ruta para 404
            self.page.go(route)
