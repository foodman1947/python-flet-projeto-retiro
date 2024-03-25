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
            usu = self.usuario.value
            sen = self.senha.value
            if usu =="":
                self.usuario.error_text="Campo de usuario vazio"
                self.update()

            elif sen =="":
                self.senha.error_text="Campo de senha vazia"
                self.update()

            elif usu =='' and sen =="":
                self.senha.error_text="preencha o login e a senha!!"
                self.update()
            elif usu == "fernando" and sen =="fernando1234@":
                print('bora para outra pagina mermão')
                self.update()
            elif usu == "joão" and sen == "91710972":
                print('bora logar joão')
                self.update()
