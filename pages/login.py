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
            if self.usuario =="":
                self.usuario.error_text="Campo de usuario vazio"
            elif self.senha =="":
                self.senha.error_text="Campo de senha vazia"
            elif self.usuario =='' and self.senha =="":
                self.senha.error_text="preencha o login e a senha!!"
            elif self.usuario == "fernando" and self.senha =="fernando1234@":
                print('bora para outra pagina mermão')
            elif self.usuario == "joão" and self.senha == "91710972":
                print('bora logar joão')