import flet as ft
import criptografia as cp
from componentes import BotaoSelecionarArquivos


def InputMensagem(mensagem_input_ref: ft.Ref[ft.TextField]):
    return ft.Container(
        ft.Column(
            controls=[
                ft.Text("Mensagem de Texto", font_family="Prompt",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                ft.TextField(
                    ref=mensagem_input_ref,
                    color=ft.colors.BLACK,
                    border_radius=ft.border_radius.all(20),
                    multiline=True,
                    min_lines=5,
                    max_lines=5,
                    bgcolor=ft.colors.WHITE,
                    border_color=ft.colors.TEAL_900,
                    focused_border_width=3
                )
            ]
        ),
        padding=ft.padding.all(20),
        border_radius=25,
        bgcolor=ft.colors.TEAL_700
    )


def InputSenha(senha_input_ref: ft.Ref[ft.TextField]):
    return ft.Container(
        ft.Column(
            controls=[
                ft.Text("Frase Senha", font_family="Prompt",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                ft.TextField(
                    ref=senha_input_ref,
                    color=ft.colors.BLACK,
                    border_radius=ft.border_radius.all(20),
                    bgcolor=ft.colors.WHITE,
                    border_color=ft.colors.TEAL_900,
                    focused_border_width=3,
                )
            ]
        ),
        padding=ft.padding.all(20),
        border_radius=25,
        bgcolor=ft.colors.TEAL_700
    )


class MenuCifrarDecifrar(ft.UserControl):
    def resultado_selecionar_arquivos(self, e: ft.FilePickerResultEvent):
        self.arquivos = list(map(lambda f: f.path, e.files)) if e.files else []

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.frase_senha = ""
        self.mensagem = ""
        self.modo_cifrar = True
        self.texto_botao = "Cifrar"
        self.botao_ref = ft.Ref[ft.ElevatedButton]()
        self.texto_botao_ref = ft.Ref[ft.Text]()
        self.input_mensagem_ref = ft.Ref[ft.TextField]()
        self.input_senha_ref = ft.Ref[ft.TextField]()
        self.botao_arquivos_ref = ft.Ref[ft.ElevatedButton]()

        self.input_senha = InputSenha(self.input_senha_ref)
        self.input_mensagem = InputMensagem(self.input_mensagem_ref)

        self.janela_selecionar_arquivos = ft.FilePicker(
            on_result=self.resultado_selecionar_arquivos)
        self.page.overlay.append(self.janela_selecionar_arquivos)

        self.arquivos: list[str] = []

    def acao_cifrar(self, e: ft.ControlEvent):
        chave = self.input_senha_ref.current.value
        texto = self.input_mensagem_ref.current.value
        texto_criptografado = cp.cifrar_mensagem(texto, chave)
        self.input_mensagem_ref.current.value = texto_criptografado
        self.update()

    def acao_decifrar(self, e: ft.ControlEvent):
        chave = self.input_senha_ref.current.value
        texto = self.input_mensagem_ref.current.value
        texto_descriptografado = cp.decifrar_mensagem(texto, chave)
        self.input_mensagem_ref.current.value = texto_descriptografado
        self.update()

    def acao_cifrar_arquivos(self, arquivos: list[str]):
        return [cp.cifrar_arquivo(arquivo, self.frase_senha) for arquivo in arquivos]

    def acao_decifrar_arquivos(self, arquivos: list[str]):
        return [cp.decifrar_arquivo(arquivo, self.frase_senha) for arquivo in arquivos]

    def selecionar_arquivos(self, e: ft.ControlEvent):
        self.janela_selecionar_arquivos.pick_files(
            allow_multiple=True,
            allowed_extensions=None if self.modo_cifrar else ["cripto"],
        )

    def acao_arquivos(self, e: ft.ControlEvent):
        return self.acao_cifrar_arquivos(self.arquivos) if self.modo_cifrar else self.acao_decifrar_arquivos(self.arquivos)

    def set_modo_cifrar(self, modo_cifrar: bool):
        self.modo_cifrar = modo_cifrar
        self.texto_botao_ref.current.value = "Cifrar" if self.modo_cifrar else "Decifrar"
        self.botao_ref.current.on_click = self.acao_cifrar if self.modo_cifrar else self.acao_decifrar
        self.update()

    def build(self) -> ft.Container:
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                width=400,
                controls=[
                    self.input_senha,
                    self.input_mensagem,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Container(
                                    ft.Text(
                                        "Cifrar", ref=self.texto_botao_ref),
                                    alignment=ft.alignment.center,
                                    width=70,
                                    padding=ft.padding.symmetric(
                                        vertical=10,
                                    ),
                                ),
                                ref=self.botao_ref,
                                on_click=self.acao_cifrar
                            ),
                            ft.ElevatedButton(
                                content=ft.Icon(ft.icons.UPLOAD_FILE),
                                ref=self.botao_arquivos_ref,
                                on_click=self.selecionar_arquivos
                            ),
                            ft.ElevatedButton(
                                content=ft.Icon(ft.icons.ARROW_RIGHT),
                                on_click=self.acao_arquivos
                            )
                        ]
                    ),
                ]
            )
        )
