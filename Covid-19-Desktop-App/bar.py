from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,OptionProperty,ListProperty,BooleanProperty,StringProperty,BoundedNumericProperty
from kivy.animation import Animation
from kivy.lang import Builder

class Bar(Widget):
    value = BoundedNumericProperty(0.,min=0,max=100)
    orientation = OptionProperty('bt',options=('lr','rl','bt','tb'))
    color = ListProperty([0.3137,0.027,0.129,1])
    background_color =ListProperty([0.07,0.1098,0.180,1])
    animated = BooleanProperty(True)
    anim_type= StringProperty('linear')
    anim_duration = NumericProperty(1.0)
    _value =  NumericProperty(0.0)
    _anim  = None

    def on_value(self,instance,value):
            if self.animated:
                if self._anim:
                    Animation.cancel_all(self)
                    self._anim = None
                a = Animation(_value = value, t=self.anim_type,d=self.anim_duration)
                a.start(self)
                self._anim =a
            else:
                self._value =  value

Builder.load_string('''
<Bar>:
    canvas:
        Color:
            rgba:root.background_color
        Rectangle:
            size: root.size
            pos: root.pos
        Color:
            rgba:root.color
        Rectangle:
            pos: self.pos if self.orientation in ('lr','bt') else (self.right - self.width*self._value/100.0,self.y) if root.orientation == 'rl' else(self.x, self.top- self.height*self._value/100.0)
            size: (self.width*self._value/100.0,self.height) if root.orientation in ('lr','rl') else (self.width, self.height*self._value/100.0)




''')
