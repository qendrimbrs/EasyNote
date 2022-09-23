from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivymd.uix.list import OneLineListItem
from kivy.uix.floatlayout import FloatLayout


# Define our different screens
class FirstWindow(Screen):
    pass


class SettingsWindow(Screen):
    pass


class MyNotesWindow(Screen):
    data_list = ListProperty()

    def list_data(self):
        data = self.data_list[-1]
        self.ids.container.add_widget(OneLineListItem(text = f"Note: {data}"))

    pass


class CreateNotesWindow(Screen):
    container = ObjectProperty(None)
    data_list = ListProperty([])

    def save_data(self, **kwargs):
        for child in reversed(self.container.children):
            if isinstance(child, TextInput):
                self.data_list.append(child.text)

        self.manager.get_screen("myNotes").data_list = list(self.data_list)
        self.manager.current = "myNotes"
        print(self.data_list)


class WindowManager(ScreenManager):
    pass


class easyNote(MDApp):
    title = "easyNote"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        return Builder.load_file('createNote.kv')


if __name__ == "__main__":
    easyNote().run()
