import flet as ft
from pages.tabum import Bvl as bv
class Pagina(ft.UserControl):

    def build(self):
        self.b = bv()
        return ft.Tabs(
            selected_index = 1,
            animation_duration= 300,
            tabs=[
                ft.Tab(
                    text="Area-Bvl",
                    content = ft.Container(
                        padding = 30,
                        expand=True,
                        content= self.b,
                ),

             
                )
                
            ],
            scrollable=True
        )