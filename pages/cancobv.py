import flet as ft
import sqlite3 as sq 

class Bvlbanc:
    def __init__(self, estoque = 0, usodiario = 0, adicionar = 0):
        self.estoque = estoque
        self.usodiario = usodiario
        self.adicionar = adicionar
        self.conn = sq.connect("bvl.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
    CREATE TABLE bvl(
                            estoque INTEGER NOT NULL,
                            usodiario INTEGER NOT NULL,
                            
    )

""")
        self.conn.commit()
    def retirarDoEstoque(self):
        pass
        
    def AdicionarNoEstoque(self):
        self.cursor.execute("SELECT estoque FROM bvl")
        a = self.cursor.fetchone()
        print(a)
        self.cursor.execute("INSERT INTO bvl(estoque)VALUE(?)", ())
        pass
    def mudarQuantidadeDiaria(self):
        pass


        
        