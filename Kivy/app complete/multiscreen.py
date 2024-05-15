from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import threading
import time
from pandas import DataFrame
from collections import OrderedDict
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.clock import Clock



#-------------------------------------------insta api-------------------------------------------
from instagrapi import Client

def logging_in(login, client = None):
    if login:
        ACCOUNT_USERNAME = username
        ACCOUNT_PASSWORD = password
        cl = Client()
        cl.delay_range = [1, 3]
        #_______________________login_______________________
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, verification_code="")    
        #_______________________create dictionary_______________________
        global a_dictionary_of_threads
        a_dictionary_of_threads = {}
        #_______________________get thread data_______________________
        thread_data = cl.direct_threads(amount=30, thread_message_limit=100)
        for i, direct_thread in enumerate(thread_data):
            ordered_dict = OrderedDict(direct_thread.__dict__)
            ordered_dict.move_to_end("users", False) #moves the user to the start of the dictionary
            current_key = []
            for x, attribute in enumerate(ordered_dict):
                if attribute == "users":
                    current_key = tuple(ordered_dict[attribute])
                    a_dictionary_of_threads[current_key] = []
                else:
                    a_dictionary_of_threads[current_key].append(ordered_dict[attribute])
        testapp.define_client(cl)
    else:
        temp_dict = {}
        thread_data = client.direct_threads(amount=30, thread_message_limit=100)
        for i, direct_thread in enumerate(thread_data):
            ordered_dict = OrderedDict(direct_thread.__dict__)
            ordered_dict.move_to_end("users", False) #moves the user to the start of the dictionary
            current_key = []
            for x, attribute in enumerate(ordered_dict):
                if attribute == "users":
                    current_key = tuple(ordered_dict[attribute])
                    temp_dict[current_key] = []
                else:
                    temp_dict[current_key].append(ordered_dict[attribute])
        a_dictionary_of_threads = temp_dict
        print("updated", testapp.sm.current)

    #root.manager.current = "ThreadsPage"
    #root.manager.transition.direction = "left"
    #-------------------------------------------insta api-------------------------------------------




def reset_table(cl):
    global testing
    testing = 0
    while True:
        logging_in(False, client=cl)
        testing += 1
        time.sleep(5)
'''
t1 = threading.Thread(target= reset_table, daemon=True)
t1.start()
'''

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{"text" : str(a_dictionary_of_threads[x][14])} for x in a_dictionary_of_threads]

class rvItem(Factory.Button):
    def get_data_index(self):
        index = self.parent.get_view_index_at(self.center)
        for i, item in enumerate(a_dictionary_of_threads):
            if i == index:
                name = str(a_dictionary_of_threads[item][1])
        testapp.sm.transition = SlideTransition(direction = "left")
        testapp.sm.current = name

    def on_press(self):
        self.get_data_index()

class LoginWindow(Screen):
    logo = "logo.png"
    def get_text(self):
        global username
        username = self.ids.username.text
        global password
        password = self.ids.password.text
        #try:
        logging_in(True)
        testapp.after_login()
        testapp.sm.transition = SlideTransition(direction="left")
        testapp.sm.current = "ThreadsPage"
        #except:
            #print("username/password is incorrect or an error occured")

class ThreadsPage(Screen):
    def create(self):
        try:
            self.box.clear_widgets()
        except:
            self.box = BoxLayout(orientation="vertical", padding=10)
        button = Button(size_hint=(0.1, 0.05), text="Logout")
        button.bind(on_press = self.switch)
        label = Label(size_hint=(1, 0.2), text="Threads")
        rv = RV()
        self.box.add_widget(button)
        self.box.add_widget(label)
        self.box.add_widget(rv)

        self.add_widget(self.box)


    def switch(self, place_holder):
        testapp.sm.transition = SlideTransition(direction = "right")
        testapp.sm.current = "LoginWindow"
    ...
    '''
    BoxLayout:
        orientation: "vertical"
        padding:10
        Button:
            size_hint: (0.1, 0.05)
            text:"Logout"
            on_press:
                root.manager.current = "LoginWindow"
                root.manager.transition.direction = "right"
        Label:
            size_hint: (1, 0.2)
            text:"Threads"
        RV:'''

class MessagePage(Screen):
    def create(self, info, scroll_prog = 0, current_text=""):
        for x in a_dictionary_of_threads:
            if x == info:
                title = a_dictionary_of_threads[x][14]
                thread_id = a_dictionary_of_threads[x][1]
                name = thread_id
        #print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        try:
            self.box.clear_widgets()
        except:
            self.box = BoxLayout(orientation="vertical")#background box layout
        back_button = Button(text="back", size_hint=(0.1, 0.05))
        back_button.bind(on_press=self.switch)
        self.box.add_widget(back_button) #adds back button 
        self.box.add_widget(Label(text=title, size_hint=(1, 0.1))) #adds title
        self.scroller = ScrollView(do_scroll_y=True, do_scroll_x=False)
        for item in a_dictionary_of_threads:
            if item == info:
                self.id = a_dictionary_of_threads[item][1]
                messages = a_dictionary_of_threads[item][2]
        grid = GridLayout(cols=2, spacing=0, size_hint_y=0.1*len(messages))
        for message in messages[::-1]:
            if message.__dict__["text"] != None:
                if message.__dict__["is_sent_by_viewer"]:
                    grid.add_widget(Button(size_hint_x=0.05))
                    label = Label(text=message.__dict__["text"], size_hint_y=None, height=40, halign="right", padding=(20, 10))
                    label.bind(size=label.setter('text_size'))  # Ensure text_size updates properly
                    grid.add_widget(label)
                else:
                    grid.add_widget(Button(size_hint_x=0.05))
                    label = Label(text=message.__dict__["text"], size_hint_y=None, height=40, halign="left", padding=(20, 10))
                    label.bind(size=label.setter('text_size'))  # Ensure text_size updates properly
                    grid.add_widget(label)
        self.scroller.add_widget(grid)
        self.scroller.scroll_y = scroll_prog
        self.box.add_widget(self.scroller)
        message_box_and_send_button = GridLayout(cols=2, size_hint_y = 0.1)
        self.message_box = TextInput(size_hint = (0.8, 1), text=current_text)
        send_button = Button(size_hint = (0.2, 1))
        send_button.bind(on_press=self.send_message)
        message_box_and_send_button.add_widget(self.message_box)
        message_box_and_send_button.add_widget(send_button)
        self.box.add_widget(message_box_and_send_button)
        if testapp.sm.current == name:
            self.message_box.focus=True
        self.add_widget(self.box)

    def switch(self, place_holder):
        testapp.sm.transition = SlideTransition(direction = "right")
        testapp.sm.current = "ThreadsPage"

    def get_scroll_value(self):
        return self.scroller.scroll_y
    
    def get_message_info(self):
        return self.message_box.text
    
    def send_message(self, place_holder):
        testapp.cl.direct_send(text=self.message_box.text, thread_ids = [self.id], send_attribute="message_button")
        self.message_box.text = ""

class TestApp(App):
    def build(self):
        self.counter = 0
        self.sm = ScreenManager()
        self.sm.add_widget(LoginWindow(name = "LoginWindow"))
        return self.sm
    def after_login(self):
        self.threadspage = ThreadsPage(name = "ThreadsPage")
        self.threadspage.create()
        self.sm.add_widget(self.threadspage)
        for item in a_dictionary_of_threads:
            self.message_page = MessagePage(name = str(a_dictionary_of_threads[item][1]))
            self.message_page.create(info=item)
            self.sm.add_widget(self.message_page)
        t1 = threading.Thread(target= reset_table,args=(self.cl,), daemon=True)
        t1.start()
        self.start_updating = True
        return self.sm
    def update(self):
        #threads page
        period = len(a_dictionary_of_threads) + 1
        while self.counter > period:
            self.counter = 1
        if self.counter == 1:
            self.threadspage.create()
        else:
            matcher = 1
            for item in a_dictionary_of_threads:
                matcher += 1
                if self.counter == matcher:
                    message_page = self.sm.get_screen(str(a_dictionary_of_threads[item][1]))
                    scroll_prog = message_page.get_scroll_value()
                    current_text = message_page.get_message_info()
                    message_page.create(info=item, scroll_prog=scroll_prog, current_text=current_text)
                    

    def define_client(self, cl):
        self.cl = cl

def my_callback(dt):
    testapp.counter += 1
    # This function will be called once per clock cycle
    try:
        if testapp.start_updating:
            testapp.update()
            #print("Muhuhuhuhuhaaa")
    except:
        pass

Clock.schedule_interval(my_callback, 0.5)

if __name__ == "__main__":  
    testapp = TestApp()
    testapp.run()  

