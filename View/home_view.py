from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.properties import ObjectProperty


Builder.load_file('View/kv_file/home_view.kv')


class HomeView(Screen):
    btn_next = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(HomeView, self).__init__(**kwargs)

        self.btn_next.bind(on_release=self.switch_next)

    def switch_next(self, *args):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = self.manager.next()

