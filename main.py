from ui import UI

ui = UI()


opcao = ""
while opcao != 0:
    ui.logoTipo()
    ui.mostraMenu()
    opcao = ui.selecionaOpcao([1, 2, 0])
    ui.limpaTela()

        ## Cadastro de filmes
    if opcao == 1:
        ui.mostraCadastroFilmes()
        opcao = ""

        ## Lista de filmes
    if opcao == 2:
        pass

