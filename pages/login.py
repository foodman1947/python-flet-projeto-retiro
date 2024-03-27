import flet as ft 
import sqlite3 

class conectLogin:
    def __init__(self, nome,senha):
        self.nome = nome
        self.senha = senha
        self.conn = sqlite3.connect("user.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                            usuario TEXT NOT NULL,
                            senha TEXT NOT NULL)""")
    def cadastrar(self):
        self.cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?,?)", (self.nome, self.senha))
        self.conn.commit()
    def consultar(self):
        self.cursor.execute("SELECT * FROM usuarios")
        resultados = self.cursor.fetchall()
        print(resultados)
        return resultados