from kivy.app import App
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
    pass


class CreateNotesWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('createNote.kv')


class EasyNote(App):
    def build(self):

        return kv


if __name__ == "__main__":
    EasyNote().run(
    )
