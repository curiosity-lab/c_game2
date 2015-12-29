from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty
import xml.etree.ElementTree as ET
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class InputForm(BoxLayout):
    title=ObjectProperty()
    body=ObjectProperty()
    checkbox_agree=ObjectProperty()
    checkbox_txt=ObjectProperty()
    button=ObjectProperty()
    def __init__(self):
        super(InputForm, self).__init__()
        dict = {'title':self.title,
                'body':self.body,
                'checkbox_txt':self.checkbox_txt,
                'button':self.button}
        f = open('agreement.xml','r', encoding='utf-8')
        txt = f.read()
        tree = ET.fromstring(txt)
        for child in tree:
            dict[child.tag].text = child.text[::-1]
            print(child.tag, child.text)

    def contin(self):
        if self.checkbox_agree.active:
            print("im working")
        else:
            print("pls mark checkbox")

    def mark_checkbox(self):
        if self.checkbox_agree.active:
            self.button.background_color = self.get_color_from_hex("#FFFFFF")
        else:
            self.button.background_color = self.get_color_from_hex("#FFC0CB")

    def get_color_from_hex(self, color):
        return get_color_from_hex(color)

