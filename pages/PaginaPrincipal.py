import flet as ft
from pages.tabum import Bvl as bv
class Pagina(ft.UserControl):

    def build(self):
        self.b = bv()
        return ft.Tabs(
            selected_index=0,
            scrollable=True,
            tabs = [
                ft.Tab(
                    text="Area-Bvl",      
                    content = self.b,
                
                ),
                ft.Tab(
                    text = "area-seila",
                    content= ft.Text('olá mundo')
                )
            ],
            expand=1
        )