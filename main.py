from ui import UI
from db import BD

ui = UI()
banco = BD("catalogoFilmes.db")

opcao = ""
while opcao != 0:
    ui.logoTipo()
    ui.mostraMenu()
    opcao = ui.selecionaOpcao([1, 2, 0])
    ui.limpaTela()

        ## Cadastro de filmes
    if opcao == 1:
        ui.mostraCadastroFilmes()

        ## Lista de filmes
    if opcao == 2:
        pass

