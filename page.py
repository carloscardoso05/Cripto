import flet
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    TextButton,
    ElevatedButton,
    ButtonStyle,
    MaterialState,
    Row,
    
)
class MainApp:
     def __init__(self, page: Page):
        self.page = page
        self.appbar = AppBar(
            title=Text("CriptoText.",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.GREEN_400,
            actions=[
                Container(
                    Row([ 
                    ElevatedButton("cifrar",
                                   height= 25,
                                   style= ButtonStyle(
                                   color= colors.GREEN_300,
                                   bgcolor= colors.WHITE,
                                   shadow_color= colors.BLACK12
                                    )
                                ),
                    ElevatedButton('decifrar',
                                   height= 25,
                                   style= ButtonStyle(
                                   color= colors.GREEN_300,
                                   bgcolor= colors.WHITE,
                                   shadow_color= colors.BLACK12,
                                   )
                                ),
                            ],
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        ),
                    bgcolor=colors.AMBER,
                    border_radius=20,
                    height= 40,
                    width= 200,
                    
                        )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
         
    
if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "CriptoText"
        page.padding = 0
        page.bgcolor = colors.WHITE
        app = MainApp(page)
        # page.add(app)
        page.update()
 
    flet.app(target=main, view=flet.WEB_BROWSER)