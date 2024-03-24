import flet as ft 

class LoginPage(ft.UserControls):
    def build(self):
        return ft.Container(
            width = 600,
            bgcolor = ft.colors.BLUe,
            content = ft.Column(
                [
                    ft.TextField(label="login"),
                    ft.TextField(label="senha", password=True, can_reveal_password=True),
                    ft.ElevatedButton('Entrar')
                ]
            ) 
        )