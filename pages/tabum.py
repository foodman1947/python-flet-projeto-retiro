import flet as ft
class Bvl(ft.UserControl):
    def build(self):
        return ft.Column(
                        [
                            ft.Row(
                                [

                                    ft.Image(
                                        src=f"../assets/bvl.png",
                                        width =350,
                                        height=350,
                                        fit= ft.ImageFit.FIT_WIDTH,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        border_radius=ft.border_radius.all(10),
                                    ),
                                    ft.Container(
                                        width = 350,
                                        height = 200,
                                        border= ft.border.all(3,ft.colors.BLACK),
                                        border_radius=ft.border_radius.all(10),
                                        content = ft.Column(
                                            [
                                                ft.Text("Em estoque: 325", size=20),
                                                ft.Text("Usados por dia: 10",size=20),
                                                ft.Text("acaba no dia: 24/04/2024", size=20)
                                            ]
                                        )

                                    )

                                ],
                                wrap=True,
                                alignment = ft.MainAxisAlignment.CENTER

                                
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton("Retirar do estoque", width=200, height=30, bgcolor=ft.colors.WHITE, color=ft.colors.BLACK, on_click = self.mudarQuantidadeDiaria ),
                                    ft.ElevatedButton("quantidade diaria", width=200, height=30, bgcolor=ft.colors.WHITE,color=ft.colors.BLACK, on_click = self.retirarEstoque),
                                    ft.ElevatedButton("Adicionar no estoque", width=200, height=30, bgcolor=ft.colors.WHITE,color=ft.colors.BLACK, on_click =self.adicionarEstoque),

                                ],
                                vertical_alignment= ft.MainAxisAlignment.CENTER,
                                alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                wrap=True,
                                scroll=ft.ScrollMode.ALWAYS,

                

                            )
                            
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER


                    )
    def adicionarEstoque(self, e):
        print('ta adicionando alguma coisa para o estoque meu mano')
    def retirarEstoque(self, e):
        print('ta retirando alguma coisa do estoque meu mano')
    def mudarQuantidadeDiaria(self, e):
        print('ta mudando a quantidade diaria meu mano')
    