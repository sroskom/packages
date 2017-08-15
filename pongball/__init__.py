from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse
from kivy.clock import Clock
from kivy.vector import Vector
import random

class PongBall(Widget):
    def __init__(self, color=[1,1,1,1], *args, **kwargs):
        super(PongBall,self).__init__(*args, **kwargs)
        self.playing = False
        self.colliders = []
        self.velocity = [1,-1]
        with self.canvas:
            Color(*color)
            self.ellipse = Ellipse(size=self.size, pos=self.pos)
    
    def serveBall(self, *args):
        self.velocity = Vector(*self.velocity).rotate(random.randint(0,90))
        self.play()

    def play(self, *args):
        if not self.playing:
            self.playing = True
            Clock.schedule_interval(self.move,1.0/60.0)

    def stop(self, *args):
        self.playing = False

    def move(self, *args):
        if self.playing:
            self.pos = Vector(*self.velocity) + self.pos
            self.ellipse.pos = self.pos
            if (self.y < 0) or (self.top > self.parent.height):
                self.velocity[1] *= -1
            if (self.x < 0) or (self.right > self.parent.width):
                self.velocity[0] *= -1
            for collider in self.colliders:
                if self.collide_widget(collider):
                    print('collision!',collider.pos)
                    if collider.bounceOnCollide:
                        self.velocity[1] *= -1
                        self.velocity[0] *= -1
                    if collider.stopOnCollide:
                        self.playing = False
        else:
            return False

    def addCollider(self, widget, stopOnCollide=False,
            bounceOnCollide=True):
        widget.stopOnCollide = stopOnCollide
        widget.bounceOnCollide = bounceOnCollide
        self.colliders.append(widget)

