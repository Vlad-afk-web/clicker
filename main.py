from kivy.app import App
from kivy.core import window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import platform
from kivy.properties import StringProperty


class MenuScreen(Screen):
  def __init__(self, **kw):
    super().__init__(**kw)

class GameScreen(Screen):
  c_click = StringProperty()
  def __init__(self, **kw):
    super().__init__(**kw)
    self.c_click = "0"
    
  def clicker(self):
    self.c_click = str(int(self.c_click) + 1) 

class MainApp(App):
  def build(self):
    sm = ScreenManager()
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(GameScreen(name='game'))
    return sm

if platform != 'android':
  Window.size = (800, 400)
  Window.top = 100


MainApp().run()