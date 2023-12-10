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
    MainAxisAlignment,
    FontWeight
    
)
class MainApp:
     def __init__(self, page: Page):
        self.page = page
        self.appbar = AppBar(
            title=Text(
                "CriptoText.",
                size=64,
                text_align="start",
                font_family= "MuseoModerno",
                color="#87E178",
                weight=FontWeight.BOLD,
                italic=True,
                ),
            center_title=False,
            toolbar_height=160,
            bgcolor='#F4F4F4',
            actions=[
                Container(
                    Row([ 
                    ElevatedButton("cifrar",
                                   height= 50,
                                   width= 165,
                                   style= ButtonStyle(
                                   color= colors.BLACK,
                                   bgcolor= "#85C7B3",
                                   shadow_color= colors.BLACK12
                                    )
                                ),
                    ElevatedButton('decifrar',
                                   height= 50,
                                   width= 165,
                                   style= ButtonStyle(
                                   color= "#797373",
                                   bgcolor= colors.TRANSPARENT,
                                   shadow_color= colors.BLACK12,
                                   )
                                ),
                            ],
                        alignment=MainAxisAlignment.SPACE_AROUND,
                        ),
                    bgcolor="#D9D9D9",
                    border_radius=40,
                    height= 76,
                    width= 385,
                    margin= 20,
                    
                        )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
         
    
if __name__ == "__main__":
 
    def main(page: Page):
        page.fonts = {
        "MuseoModerno": "https://fonts.googleapis.com/css2?family=MuseoModerno:wght@500&display=swap"
    }

        page.title = "CriptoText"
        page.padding = 0
        page.bgcolor = "#688787"
        app = MainApp(page)
        # page.add(app)
        page.update()
 
    flet.app(target=main, view=flet.WEB_BROWSER)