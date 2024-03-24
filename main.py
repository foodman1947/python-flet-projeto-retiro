import flet as ft
from pages.login import LoginPage as lp

def main(page: ft.Page):
    login = lp()
    page.add(login)

ft.app(main)
