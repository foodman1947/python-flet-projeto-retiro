import flet as ft
from pages.login import LoginPage as lp

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    login = lp()
    page.add(login)
    
ft.app(main)
