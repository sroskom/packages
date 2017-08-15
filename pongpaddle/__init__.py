from kivy.uix.widget import Widget
from kivy.graphics import Color,Rectangle

class PongPaddle(Widget):
    def __init__(self, color=[1,1,1,1], *args, **kwargs):
        super(PongPaddle,self).__init__(*args, **kwargs)
        self.touch_y = 0
        self.center_y_marker = self.center_y
        with self.canvas:
            Color(*color)
            self.rect = Rectangle(size=self.size,
                    pos=self.pos)
    
    def on_touch_down(self, touch):
        self.touch_y = touch.y
        self.center_y_marker = self.center_y

    def on_touch_move(self, touch):
        self.center_y = self.center_y_marker + (touch.y - self.touch_y)
        if self.y < 0:
            self.y = 0
        elif self.top > self.parent.height:
            self.top = self.parent.height
        self.rect.pos = self.pos

    def anchorRight(self):
        self.x = self.parent.width - self.width

    def anchorLeft(self):
        self.x = self.parent.x

