from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class Threads(BoxLayout):
    def __init__(self, **kwargs):
        super(Threads, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.rv = RecycleView(size_hint=(1, None), size=(400, 400))
        self.add_widget(self.rv)
        self.data = [{"text":str(i)} for i in range(20)]

    def switch(self, instance):
        myapp.screen_manager.current = "second"

    def add_buttons(self):
        for item in self.data:
            button = Button(text=item['text'])
            button.bind(on_press=self.switch)
            self.rv.add_widget(button)

class Messages(BoxLayout):
    def __init__(self, **kwargs):
        super(Messages, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.rv = RecycleView(size_hint=(1, None), size=(400, 400))
        self.add_widget(self.rv)
        self.data = [{"text":"yoo"}]

    def switch(self, instance):
        myapp.screen_manager.current = "first"

    def add_buttons(self):
        for item in self.data:
            button = Button(text=item['text'])
            button.bind(on_press=self.switch)
            self.rv.add_widget(button)

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.first_page = Threads()
        self.first_page.add_buttons()
        screen = Screen(name="first")
        screen.add_widget(self.first_page)
        self.screen_manager.add_widget(screen)

        self.second_page = Messages()
        self.second_page.add_buttons()
        screen = Screen(name="second")
        screen.add_widget(self.second_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
