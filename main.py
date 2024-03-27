import flet as ft
from pages.login import conectLogin as ct
from pages.PaginaPrincipal import Pagina as pg

def main(page: ft.Page):
    page.theme_mode = "dark"
   
    def mudancaDeRota(route):
        page.views.clear()
        def ida(e):
            if nome.value == "joão" and senha.value =="91710972":
                page.go("/paginaPrincipal")
            elif nome.value == "fernando" and senha.value == "fernando123@":
                page.go("/paginaPrincipal")
            else:
                nome.error_text = "há algo de errado com seu login ou senha"
                page.update()

        def cad(e):
            page.go("/cadastro")
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Container(
                        width=600,
                        bgcolor=ft.colors.BLUE,
                        content=ft.Column(
                            [
                                nome:=ft.TextField(label='nome de usuario'),
                                senha:=ft.TextField(label="senha"),
                                ft.Row([ft.ElevatedButton('Cadastrar', on_click=cad),ft.ElevatedButton("entrar", on_click=ida)], alignment= ft.CrossAxisAlignment.END)
                            ]
                        )
                    )
                ], vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            )
        )
        
        if page.route == "/paginaPrincipal":
            page.views.append(
                ft.View(
                    "/paginaPrincipal",
                    [
                        ft.Text('oi')
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                )
            )
        elif page.route == "/cadastro":
            page.views.append(
                ft.View(
                    "/cadastro",
                    [
                        ft.Container(
                            width=600,
                            bgcolor= ft.colors.BLUE,
                            content=ft.Column(
                                [
                                    
                                ]
                            )
                        )
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
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
