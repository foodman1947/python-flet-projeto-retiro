import flet as ft
from pages.login import LoginPage as lp
from pages.PaginaPrincipal import Pagina as pg

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    login = lp()
    login.verificarLogin(page)
    principal = pg()
    def mudancaDeRota(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    login
                ]
            )
        )
        if page.route == "/paginaPrincipal":
            page.views.append(
                ft.View(
                    "/paginaPrincipal",
                    [
                        principal
                    ]
                )
            )
            page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = mudancaDeRota
    page.on_view_pop = view_pop
    page.go(page.route)
ft.app(main)
