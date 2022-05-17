from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty


Builder.load_file('View/kv_file/home_view.kv')


class HomeView(Screen):
    M_BACKGROUND_COLOR = ListProperty([1, .2, .2, .2])
    M_BORDER_COLOR = ListProperty([0, 0, 0, 1])
    M_TEXT_COLOR = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(HomeView, self).__init__(**kwargs)

        self.home_btn_edit.bind(on_release=self.switch_next)

    def switch_next(self, *args):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = self.manager.next()


