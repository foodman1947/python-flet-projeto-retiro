import flet as ft

class Pagina(ft.UserControl):
    def build(self):
        return ft.Container(
            width = 900,
            height = 900,
            padding = 20,
            content=ft.Column(
                [
                    ft.Row(
                        [

                            ft.Image(
                                src=f"../assets/bvl.png",
                                width = 300,
                                height = 300,
                                fit= ft.ImageFit.NONE,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                                border_radius=ft.border_radius.all(10),
                            ),
                            ft.Container(
                                width = 600,
                                height = 300,
                                border= ft.border.all(3,ft.colors.BLACK),
                                border_radius=ft.border_radius.all(10),
                                content = ft.Column(
                                    [
                                        ft.Text("Quantidade de sacos bvl em estoque: 325", size=30),
                                        ft.Text("Qauntidade usadas pro dia: 10",size=30),
                                        ft.Text("O estoque está previsto para acabar no dia: 24/04/2024", size=30)
                                    ]
                                )

                            )

                        ]
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("Retirar do estoque", width=200, height=100, bgcolor=ft.colors.WHITE, color=ft.colors.BLACK),
                            ft.ElevatedButton("quantidade diaria", width=200, height=100, bgcolor=ft.colors.WHITE,color=ft.colors.BLACK),
                            ft.ElevatedButton("estoque", width=200, height=100, bgcolor=ft.colors.WHITE,color=ft.colors.BLACK ),

                        ],
                        width = 900,
                        height = 400,
                        vertical_alignment= ft.MainAxisAlignment.CENTER,
                        alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
        

                    )
                    
                ], alignment = ft.CrossAxisAlignment.CENTER,
            )
        )