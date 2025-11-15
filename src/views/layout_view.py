import flet as ft
from typing import List
from components.navigation_bar import NavBar


class LayoutView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        route: str,
        controls: List[ft.Control] | None = None,
        appbar: ft.AppBar | None = None,
        padding: int | None = 10,
        **kwargs,
    ):
        self.page = page

        nav_bar = NavBar(page=self.page).build() # type: ignore

        super().__init__(
            route=route,
            navigation_bar=nav_bar,
            appbar=appbar,
            controls=controls or [],
            padding=padding,
            **kwargs,
        )