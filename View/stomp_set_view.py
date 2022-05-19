from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition

from Model import UI_STYLE
import AppConstant


class StompSettingView(Screen):
    def __init__(self, **kwargs):
        super(StompSettingView, self).__init__(**kwargs)

        main_boxlayout = BoxLayout(orientation='vertical')

        btn_back = Button()
        btn_back.size_hint = (0.2, 0.2)
        btn_back.color = UI_STYLE.M_TEXT_COLOR
        btn_back.background_color = UI_STYLE.M_BUTTON_COLOR
        btn_back.text = 'BACK'
        btn_back.bind(on_release=self.event_goto_home)

        self.lbl_bank_name = Label()
        self.lbl_bank_name.color = UI_STYLE.M_TEXT_COLOR
        self.lbl_bank_name.text = 'Distortion'

        main_boxlayout.add_widget(btn_back)
        main_boxlayout.add_widget(self.lbl_bank_name)
        self.add_widget(main_boxlayout)

    def event_goto_home(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = AppConstant.SCREEN_HOME


