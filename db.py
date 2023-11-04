import sqlite3

class BD:
    def __init__(self, banco_dados):
        self.banco = ""
        self.cursor = ""

    def concetarBanco(self, banco_dados):
        self.banco = sqlite3.connect('')
        self.cursor = self.banco.cursor()

        self.criarTabelaFilmes()
        
    def criarTabelaFilmes(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                id INTERGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL, 
                genero TEXT NOT NULL,
                duracao TEXT NULL,
                diretor TEXT NULL,
                estudio TEXT NULL,
                classificacao TEXT NULL,
                ano DATE NULL
            )


                """)