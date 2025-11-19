import flet as ft


class Title(ft.Text):
    def __init__(self, value: str, size: int = 28, **kwargs):
        super().__init__(value=value, size=size, weight=ft.FontWeight.BOLD, **kwargs)
