import flet as ft 

class LoginPage(ft.UserControl):
    def build(self):
        self.usuario=ft.TextField(label="login")
        self.senha=ft.TextField(label="senha", password=True, can_reveal_password=True)     

        return ft.Container(
            width = 300,
            bgcolor = ft.colors.BLUE,
            padding = 30,
            border_radius=6,
            content = ft.Column(
                [
                    self.usuario,
                    self.senha,
                    ft.Row([ft.ElevatedButton('Entrar', on_click=self.verificarLogin)], vertical_alignment=ft.MainAxisAlignment.END)
                ]
            ) 
        )
    def verificarLogin(self, e):
            pass