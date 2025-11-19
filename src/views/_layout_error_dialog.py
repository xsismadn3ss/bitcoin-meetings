from typing import List
import flet as ft
from ._layout_base import BaseLayout
from enum import Enum


class ErrorLevel(Enum):
    DANGER = "danger"
    WARNING = "warning"


class ErrorColors(Enum):
    LIGHT_DANGER = "#FFEDED"
    DARK_DANGER = "#391212"
    LIGHT_WARNING = "#FFECE3"
    DARK_WARNING = "#3A1F10"


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
        level: ErrorLevel = ErrorLevel.DANGER,
        height: int = 75,
    ):
        brightness = self.page.platform_brightness  # type: ignore
        is_dark = brightness == ft.Brightness.DARK

        bg = ft.Colors.ON_PRIMARY
        color = ft.Colors.PRIMARY

        if level == ErrorLevel.DANGER:
            bg = ErrorColors.DARK_DANGER if is_dark else ErrorColors.LIGHT_DANGER
            color = ft.Colors.RED
        if level == ErrorLevel.WARNING:
            color = ft.Colors.ORANGE
            bg = ErrorColors.DARK_WARNING if is_dark else ErrorColors.LIGHT_WARNING

        modal = ft.AlertDialog(
            title=ft.Text(title, color=color, weight=ft.FontWeight.BOLD),
            bgcolor=bg.value,  # type: ignore
            content=ft.Column(
                [
                    ft.Text(
                        f"• {e}",
                        color=color,
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
