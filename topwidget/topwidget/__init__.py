from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class Top(Widget):
    def __init__(self, *args, **kwargs):
        super(Top,self).__init__(*args, **kwargs)
        self.size = Window.size
        with self.canvas:
            Color(*[1,.95,.8,1])
            Rectangle(size=self.size)
    
