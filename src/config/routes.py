import flet as ft
from typing import Dict, Callable

from views.home_view import HomeView
from views.profile_view import ProfileView
from views.login_view import LoginView
from views.register_view import RegisterView

routes: Dict[str, Callable[[ft.Page], ft.View]] = {
    "/": lambda p: HomeView(p),
    "/profile": lambda p: ProfileView(p),
    "/login": lambda p: LoginView(p),
    "/register": lambda p: RegisterView(p)
}
