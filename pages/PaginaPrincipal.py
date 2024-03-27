import flet as ft

class Pagina(ft.UserControl):
    def build(self):
        return ft.Container(
            width=900,
            bgcolor = ft.colors.RED,
            content=ft.Column(
                [
                    ft.TextField(label="olá você está na pagina principal")
                ]
            )
        )