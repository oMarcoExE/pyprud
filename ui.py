import os
from db import BD

#classe para interface

class UI:
    def __init__(self):
        self.banco = BD("catalogoFilmes.db")


    def logoTipo(self):
        print("=====================================")
        print("======== Catalago de Filmes =========")
        print("=====================================")
        print()

    def mostraMenu(self):
        print("1- Cadastrar Filme")
        print("2- Lista de Filmes")
        print("0- Sair")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def selecionaOpcao(self, opcoes = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoes)

        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção invalida")
            return self.selecionaOpcao(opcoes)

        if opcaoSelecionada not in opcoes:
            print("Opção Invalida!")
            return self.selecionaOpcao(opcoes)

        return opcaoSelecionada
    
    def mostraCadastroFilmes(self):
        self.logoTipo()

        print("Insira os dados do filme:")
        print("campos com * são obrigatórios")
        
        titulo = self.solicitaValor("Digite o titulo* ", 'texto', False)
        genero = self.solicitaValor("Digite o gênero* ", 'texto', False)
        duracao = self.solicitaValor("Digite a duracao ", 'numero', True)
        diretor = self.solicitaValor("Digite o diretor ", 'texto', True)
        estudio = self.solicitaValor("Digite a estudio ", 'texto', True)
        classificacao = self.solicitaValor("Digite a classificacao ", 'texto', True)
        ano = self.solicitaValor("Digite o ano ", 'numero', True)

        valores = {
            "titulo": titulo,
            "genero": genero,
            "duracao": duracao,
            "diretor": diretor,
            "estudio": estudio,
            "classificacao": classificacao,
            "ano": ano,
        }

        self.banco.inserir('filmes', valores)


    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
           return valor
       
        if tipo == 'numero':
            try:
               valor = float(valor)
            except ValueError:
               print("Valor invalida!")
               return self.solicitaValor(legenda, tipo, permiteNulo)
        return valor

