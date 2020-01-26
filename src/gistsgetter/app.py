"""
An application dedicated to creating, editing, and deleting Gists in GitHub
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .common.GetUrlToken import get_token
from .common.Search import search
from functools import partial


class GistsGetter(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        top_box = toga.Box(style=Pack(direction=ROW, padding=5, flex=1))

        select_label = toga.Label('Search By', style=Pack(padding=5, alignment='center'))
        select = toga.Selection(items=['UserID','GistID'])
        select_input = toga.TextInput(style=Pack(padding=5, flex=1),placeholder='User or Gist ID')
        select_button = toga.Button('Search',style=Pack(padding=5),on_press=partial(search, 'x'))

        top_box.add(select_label)
        top_box.add(select)
        top_box.add(select_input)
        top_box.add(select_button)

        main_box.add(top_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return GistsGetter()
