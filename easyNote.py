from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


# Define our different screens
class FirstWindow(Screen):
    pass


class SettingsWindow(Screen):
    pass


class MyNotesWindow(Screen):
    data_list = ListProperty()

    def list_data(self):
        print(self.data_list)

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


kv = Builder.load_file('createNote.kv')


class EasyNote(App):
    def build(self):
        return kv


if __name__ == "__main__":
    EasyNote().run(
    )
