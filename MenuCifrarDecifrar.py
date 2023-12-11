import flet as ft

class MenuCifrarDecifrar(ft.UserControl):
    def __init__(self, frase_senha: str = "", mensagem: str = "", modo_cifrar: bool = True) -> None:
        super().__init__()
        self.frase_senha = frase_senha
        self.mensagem = mensagem
        self.modo_cifrar = modo_cifrar
        self.botao_texto = ft.Text("Cifrar",font_family="Baumans") 

        def set_frase_senha(e: ft.ControlEvent):
            self.frase_senha = e.control.value

        def set_mensagem(e: ft.ControlEvent):
            self.mensagem = e.control.value

        self.input_frase_senha = ft.Container(
            ft.Column(
                controls=[
                    ft.Text("Frase Senha", font_family="Prompt",
                            weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                    ft.TextField(
                        border_radius=ft.border_radius.all(20),
                        bgcolor=ft.colors.WHITE,
                        border_color=ft.colors.TEAL_900,
                        focused_border_width=3,
                        on_change=set_frase_senha
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
                    border_radius=ft.border_radius.all(20),
                    multiline=True,
                    min_lines=5,
                    bgcolor=ft.colors.WHITE,
                    border_color=ft.colors.TEAL_900,
                    focused_border_width=3,
                    on_change=set_mensagem
                )
            ]
        ),
        padding=ft.padding.all(20),
        border_radius=25,
        bgcolor=ft.colors.TEAL_700
    )
        
    def set_modo_cifrar(self, modo_cifrar: bool):
        self.modo_cifrar = modo_cifrar
        self.botao_texto.value = "Cifrar" if self.modo_cifrar else "Decifrar"
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
                                    self.botao_texto,
                                    padding=ft.padding.symmetric(
                                        vertical=10, horizontal=20)
                                )
                            ),
                            ft.IconButton(icon=ft.icons.UPLOAD_FILE_OUTLINED)
                        ]
                    ),
                ]
            )
        )
