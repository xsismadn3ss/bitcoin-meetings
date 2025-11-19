import flet as ft
from typing import List


class BaseLayout(ft.View):
    """Plantilla base para vistas

    Esta plantilla contiene métodos para abrir y cerrar díalogos
    """

    def __init__(
        self,
        page: ft.Page,
        route: str,
        controls: List[ft.Control] | None = None,
        appbar: ft.AppBar | None = None,
        padding: ft.Padding = ft.padding.only(top=30, bottom=10, left=10, right=10),
        **kwargs,
    ):
        self.page = page

        super().__init__(
            route=route,
            appbar=appbar,
            controls=controls or [],
            padding=padding,
            **kwargs,
        )

    def open_dialog(self, dialog: ft.AlertDialog):
        """Abrir díalogo

        Args:
            dialog (ft.AlertDialog): díalogo
        """
        self.page.open(dialog)  # type: ignore
        self.page.update()  # type: ignore

    def close_dialog(self, dialog: ft.AlertDialog):
        """Cerrar díalogo

        Args:
            dialog (ft.AlertDialog): díalogo
        """
        self.page.close(dialog)  # type: ignore
        self.page.update()  # type: ignore
