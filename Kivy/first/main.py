from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class MainBox(BoxLayout):
    pass

class LoginScreen(GridLayout):
    pass

class HelloApp(App):
    pass
    #def build(self):
        #return LoginScreen()
    
if __name__ == "__main__":
    myApp = HelloApp()
    myApp.run()