"""
An application dedicated to creating, editing, and deleting Gists in GitHub
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
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
        main_box = toga.Box(style=Pack(direction=COLUMN))
        top_box = toga.Box(style=Pack(direction=ROW, padding=5, alignment='top', flex=0))
        middle_box = toga.Box(style=Pack(padding=5, alignment='center', flex=1))
        bottom_box = toga.Box(style=Pack(direction=ROW, padding=(5,5,20,5), alignment='bottom', flex=0)) # Padding - Top, Right, Botom, Left

        select_label = toga.Label('Search By', style=Pack(padding=5, alignment='center'))
        self.select = toga.Selection(items=['UserID','GistID'])
        self.select_input = toga.TextInput(style=Pack(padding=5, flex=1),placeholder='User or Gist ID')
        # Line preserved for prostarity will be using helper functions to do search with externale functions
        # select_button = toga.Button('Search',style=Pack(padding=5),on_press=partial(search,string = 'x'))
        select_button = toga.Button('Search', style=Pack(padding=5), on_press=self.search_by)

        self.results = toga.MultilineTextInput(style=Pack(padding=(0,5), flex=1),readonly = True)

        middle_box.add(self.results)

        top_box.add(select_label)
        top_box.add(self.select)
        top_box.add(self.select_input)
        top_box.add(select_button)

        login_label = toga.Label('Username', style=Pack(padding=5, alignment='left'))
        self.login_input = toga.TextInput(style=Pack(padding=5,alignment='left',flex=1))
        pw_label = toga.Label('Password', style=Pack(padding=5, alignment='right'))
        self.pw_input = toga.PasswordInput(style=Pack(padding=4,alignment='right',flex=1))

        bottom_box.add(login_label)
        bottom_box.add(self.login_input)
        bottom_box.add(pw_label)
        bottom_box.add(self.pw_input)

        main_box.add(top_box)
        main_box.add(middle_box)
        main_box.add(bottom_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def search_by(self, widget):

        if not self.select_input.value or not self.login_input.value or not self.pw_input:
            self.results.value = 'All fields required'
            return
        if self.select.value == 'UserID':
            self.results.value = 'Feature not implemented'
            return
        else:
            global gist_id
            gist_id = self.select_input.value
            url = self.__get_token('https://api.github.com/gists{/gist_id}','{')
            results = search(url, self.login_input.value,self.pw_input.value)
            self.results.value = results


    def __get_token(self, string, delim):
   
        tokens = string.split(delim)
        url = tokens[0]
        
        for token in tokens[1:]:
            token = token[:-1]
            if '/' in token : token = token[1:]
            if token in globals():
                if '=' in url:
                    url = url + globals()[token]
                else:
                    url = url + '/' + globals()[token]
            if ',' in token:
                token = token[1:]
                print(token)
                multitokens = token.split(',')
                for multitoken in multitokens:
                    if multitoken in globals():
                        url =  url + '&' + multitoken + '=' + globals()[multitoken]
        return url

def main():
    return GistsGetter()
