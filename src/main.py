import flet as ft
from config.theme import scheme
from service.router import Router


def main(page: ft.Page):
    page.title = "Bitcoin Meetings"

    page.theme = ft.Theme(color_scheme=scheme)

    router = Router(page=page)
    page.on_route_change = router.route_change
    page.on_view_pop = router.view_pop

    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)
