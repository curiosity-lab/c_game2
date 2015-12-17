import kivy
kivy.require('1.9.0')  # replace with your current kivy_tests version !
from kivy.app import App
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from functools import partial
import socket
import xml.etree.ElementTree as ET

#agreement = ET.parse('agreement.xml')
#root_agreement = agreement.getroot()
#details = ET.parse('details.xml')
#root_details = details.getroot()

class MyApp(App):
#    connection = None
#    server_list = ['192.168.43.52'] #['192.168.43.94','192.168.43.52','192.168.1.102', '192.168.1.101', '192.168.1.1']
#    port = 12345

    def build(self):

        wid = Widget()
        curiosity_q = ET.parse('curiosity_q.xml')
        root_curiosity_q = curiosity_q.getroot()
        label1 = Label(root_curiosity_q[0][0].text)
        #button = Button(text='Connect...', on_press=partial(self.connect, label))
        textbox = TextInput(size_hint_y=.1, multiline=False)
        textbox.bind(on_text_validate=partial(self.send_message, textbox, label))
        layout = BoxLayout()
        layout.add_widget(label)
        #layout.add_widget(button)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


    def print_message(self, msg, label):
        label.text += str(msg) + "\n"

if __name__ == '__main__':
    MyApp().run()