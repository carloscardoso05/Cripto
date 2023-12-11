import flet as ft
import criptografia as cp

class MenuCifrarDecifrar(ft.UserControl):

    def acao_cifrar(self, e: ft.ControlEvent):
        chave = self.senha_input_ref.current.value
        texto = self.mensagem_input_ref.current.value
        texto_criptografado = cp.cifrar(texto, chave)
        self.mensagem_input_ref.current.value = texto_criptografado
        self.update()

    def acao_decifrar(self, e: ft.ControlEvent):
        chave = self.senha_input_ref.current.value
        texto = self.mensagem_input_ref.current.value
        texto_descriptografado = cp.decifrar(texto, chave)
        self.mensagem_input_ref.current.value = texto_descriptografado
        self.update()


    def __init__(self) -> None:
        super().__init__()
        self.frase_senha = ""
        self.mensagem = ""
        self.modo_cifrar = True
        self.texto_botao = "Cifrar"
        self.botao_ref = ft.Ref[ft.ElevatedButton]()
        self.texto_botao_ref = ft.Ref[ft.Text]()
        self.mensagem_input_ref = ft.Ref[ft.TextField]()
        self.senha_input_ref = ft.Ref[ft.TextField]()



        self.input_frase_senha = ft.Container(
            ft.Column(
                controls=[
                    ft.Text("Frase Senha", font_family="Prompt",
                            weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                    ft.TextField(
                        ref = self.senha_input_ref,
                        color = ft.colors.BLACK,
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
        self.input_mensagem = ft.Container(
        ft.Column(
            controls=[
                ft.Text("Mensagem de Texto", font_family="Prompt",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                ft.TextField(
                    ref = self.mensagem_input_ref,
                    color = ft.colors.BLACK,
                    border_radius=ft.border_radius.all(20),
                    multiline=True,
                    min_lines=5,
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
                    self.input_frase_senha,
                    self.input_mensagem,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Container(
                                    ft.Text("Cifrar", ref=self.texto_botao_ref),
                                    padding=ft.padding.symmetric(
                                        vertical=10, horizontal=20),
                                ),
                                ref = self.botao_ref,
                                on_click=self.acao_cifrar
                            ),
                            ft.IconButton(icon=ft.icons.UPLOAD_FILE_OUTLINED)
                        ]
                    ),
                ]
            )
        )
