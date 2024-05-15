from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.textinput import TextInput


class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")
        label = Label(text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",size = (200, 200), size_hint_x = 1)
        label.text_size = label.size
        label.multiline = True

        box.add_widget(label)
        self.add_widget(box)

    
class MyApp(App):
    def build(self):
        # Create a screen manager
        sm = ScreenManager()
        # Add screens to the screen manager
        self.screen1 = Screen1(name='screen1')
        sm.add_widget(self.screen1)
        self.start = True
        return sm
    
if __name__ == '__main__':
    test = MyApp()
    test.run()

