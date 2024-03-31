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
                                        fit= ft.ImageFit.COVER,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        border_radius=ft.border_radius.all(10),
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3,ft.colors.BLACK),
                                        border_radius=ft.border_radius.all(10),
                                        content = ft.Column(
                                            [
                                                ft.Text("Em estoque: 325", size=30),
                                                ft.Text("Usados por dia: 10",size=30),
                                                ft.Text("O estoque acaba no dia: 24/04/2024", size=30)
                                            ]
                                        )

                                    )

                                ],
                                wrap=True,
                                scroll=ft.ScrollMode.ALWAYS,
                                alignment=ft.MainAxisAlignment.CENTER,

                                
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton("Retirar do estoque", width=300, height=100, bgcolor=ft.colors.WHITE, color=ft.colors.BLACK),
                                    ft.ElevatedButton("quantidade diaria", width=300, height=100, bgcolor=ft.colors.WHITE,color=ft.colors.BLACK),
                                    ft.ElevatedButton("estoque", width=300, height=100, bgcolor=ft.colors.WHITE,color=ft.colors.BLACK ),

                                ],
                                vertical_alignment= ft.MainAxisAlignment.CENTER,
                                alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                wrap=True,
                                scroll=ft.ScrollMode.ALWAYS,

                

                            )
                            
                        ], alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.ALWAYS,
                        on_scroll_interval=0,


                    )