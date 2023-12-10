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
    margin
)
# class TrelloApp:
#     def __init__(self, page: Page):
#         self.page = page
#         self.appbar_items = [
#             PopupMenuItem(text="Login"),
#             PopupMenuItem(),  # divider
#             PopupMenuItem(text="Settings")
#         ]
#         self.appbar = AppBar(
#             leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
#             leading_width=100,
#             title=Text("Trolli",size=32, text_align="start"),
#             center_title=False,
#             toolbar_height=75,
#             bgcolor=colors.LIGHT_BLUE_ACCENT_700,
#             actions=[
#                 Container(
#                     content=PopupMenuButton(
#                         items=self.appbar_items
#                     ),
#                     margin=margin.only(left=50, right=25)
#                 )
#             ],
#         )
#         self.page.appbar = self.appbar
#         self.page.update()
class MainApp:
     def __init__(self, page: Page):
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            title=Text("CriptoText.",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.GREEN_800,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
         
    
if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = MainApp(page)
        # page.add(app)
        page.update()
 
    flet.app(target=main, view=flet.WEB_BROWSER)