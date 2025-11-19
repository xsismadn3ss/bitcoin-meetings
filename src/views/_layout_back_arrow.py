import flet as ft
from components.title import Title
from ._layout_base import BaseLayout
from typing import List


class LayoutBackArrow(BaseLayout):
    """Plantilla con flecha de volver hacia atras en la
    parte superior de la interfaz de usuario
    """

    def __init__(
        self,
        page: ft.Page,
        title: str,
        route: str,
        back_route,
        controls: List[ft.Control] | None = None,
        padding: ft.Padding = ft.padding.only(),
        **kwargs,
    ):
        view_title = Title(title)
        back_btn = ft.IconButton(
            ft.Icons.ARROW_BACK, on_click=lambda e: page.go(back_route)
        )
        header = ft.Container(
            ft.Row([back_btn, view_title]),
            padding=ft.padding.only(top=10, bottom=10, left=5, right=5),
            border=ft.Border(
                bottom=ft.BorderSide(
                    width=0.5,  # Grosor (1.5px)
                    color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                )
            ),
            margin=ft.margin.only(bottom=20),
        )
        c = [
            header,
            ft.Container(
                ft.Column(controls), padding=ft.padding.only(left=20, right=20)
            ),
        ]
        super().__init__(page, route, c, padding=padding, **kwargs)  # type: ignore
