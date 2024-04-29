from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        return Label(text="hello world")
    
if __name__ == "__main__":
    MyApp().run()