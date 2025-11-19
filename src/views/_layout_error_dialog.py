from typing import List
import flet as ft
from ._layout_base import BaseLayout


class LayoutErrorDialog(BaseLayout):
    def __init__(
        self,
        page: ft.Page,
        route: str,
        controls: List[ft.Control] | None = None,
        **kwargs,
    ):
        super().__init__(page, route, controls, **kwargs)

    def build_error_dialog(
        self,
        errors: list[str] = [],
        title: str = "Error",
        color: ft.ColorValue | None = ft.Colors.RED,
        bgcolor: ft.ColorValue | None = ft.Colors.with_opacity(0.2, ft.Colors.RED),
        height: int = 75
    ):
        brightness = self.page.platform_brightness  # type: ignore
        is_dark = brightness == ft.Brightness.DARK

        modal = ft.AlertDialog(
            # modal=True,
            title=ft.Text(title, color=color, weight=ft.FontWeight.BOLD),
            bgcolor=bgcolor if is_dark else None,
            content=ft.Column(
                [
                    ft.Text(
                        f"• {e}",
                        color=color if is_dark else None,
                        weight=ft.FontWeight.W_500,
                    )
                    for e in errors
                ],
                scroll=ft.ScrollMode.ADAPTIVE,
                height=height,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                tight=True,
            ),
            actions=[
                ft.TextButton(
                    "cerrar",
                    on_click=lambda e: self.close_dialog(modal),
                    style=ft.ButtonStyle(
                        color=color,
                        overlay_color=ft.Colors.with_opacity(0.3, color),  # type: ignore
                    ),
                )
            ],
        )
        return modal
