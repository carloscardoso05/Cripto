import flet as ft
from componentes import *

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # função de exemplo
    def salvar_caminhos(caminhos:list[str]):
        print(caminhos)

    page.add(
        ft.Column([
            # exemplo de uso do botão de selecionar arquivos
            BotaoSelecionarArquivos(page=page, on_selected=salvar_caminhos, extensoes_permitidas=['pdf'],)
        ])
    )


ft.app(target=main)
