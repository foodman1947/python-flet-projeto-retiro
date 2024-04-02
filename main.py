import flet as ft
from pages.login import conectLogin as ct
from pages.tabum import Bvl as bv
from time import sleep

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ALWAYS
    bbb = bv()
    viewli = ft.Column(scroll=ft.ScrollMode.ALWAYS)
    viewli.controls.append(bbb)
    page.theme_mode = "dark"
    def mudancaDeRota(route):
        page.views.clear()
        def logi(e):
            if sen.value == consen.value and sen.value != "" and consen.value != "":
                bc = ct(nme.value, sen.value)
                bc.cadastrar()
                bc.consultar()
                page.go("/")
                        
            else:
                sen.error_text = "Senhas não correspondem"
                consen.error_text = "senhas não correspondem"
                page.update()
            pass
        def ida(e):

            bc = ct(nome.value, senha.value)
            coulta = bc.consultar()
            for i in coulta:
                if nome.value == i[0] and senha.value == i[1]:
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
                        width=400,
                        bgcolor=ft.colors.BLUE,
                        padding = 30,
                        content=ft.Column(
                            [
                                nome:=ft.TextField(label='nome de usuario'),
                                senha:=ft.TextField(label="senha", password=True, can_reveal_password=True),
                                ft.Row([ft.ElevatedButton('Cadastrar', on_click=cad),ft.ElevatedButton("entrar", on_click=ida)], alignment= ft.CrossAxisAlignment.END)
                            ]
                        )
                    )
                ],vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            )
        )
        def mudanca(e):
            viewli.clean()
            if tab.selected_index == 0:
                viewli.controls.append(bbb)
                page.update()
            elif tab.selected_index == 1:
                viewli.controls.append(ft.Text('olá mundo'))
                page.update()

            else:
                viewli.controls.append(ft.Text('olá mundo2'))
                page.update()

        if page.route == "/paginaPrincipal":
            page.views.append(
                ft.View(
                    "/paginaPrincipal",
                    [
                        ft.Column(
                            [
                                tab:=ft.Tabs(
                                    selected_index=0,
                                    tabs =[
                                        a1:= ft.Tab(
                                            text = "area-bvl",
                                            content = ""
                                        ),
                                        a2:= ft.Tab(
                                            text="area-silo",
                                            content= ""
                                        ),
                                        a3:=ft.Tab(
                                            text="area-trator",
                                            content = ""
                                        )
                                    ],
                                    on_change= mudanca,
                                    scrollable = True,
                                    
                                ),
                                viewli

                            ]
                        )
                        
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS
            
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
                                    nme:=ft.TextField(label="usuario"),
                                    sen:=ft.TextField(label="criar senha"),
                                    consen:=ft.TextField(label="confirmar senha"),
                                    ft.ElevatedButton('Confirmar', on_click=logi)                                  
                                ]
                            )
                        )
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS
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