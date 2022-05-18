from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.properties import ObjectProperty

from Model import UI_STYLE


class HomeView(Screen):

    def __init__(self, **kwargs):
        super(HomeView, self).__init__(**kwargs)

        main_boxlayout = BoxLayout(orientation='vertical')

        main_boxlayout.add_widget(self.ui_effect_chain())
        main_boxlayout.add_widget(self.ui_status())
        self.add_widget(main_boxlayout)

    def ui_effect_chain(self):
        self.chain_layout = GridLayout()
        self.chain_layout.size_hint = (1, 0.85)

        return self.chain_layout

    def ui_status(self):
        status_layout = BoxLayout()
        status_layout.orientation = 'horizontal'
        status_layout.size_hint = (1, 0.15)

        self.btn_bank_bank = Button()
        self.btn_bank_bank.size_hint = (0.1, 1)
        self.btn_bank_bank.color = UI_STYLE.M_TEXT_COLOR
        self.btn_bank_bank.background_color = UI_STYLE.M_BUTTON_COLOR
        self.btn_bank_bank.text = 'A1'
        self.btn_bank_bank.bind(on_release=self.switch_bank_select)

        self.lbl_bank_name = Label()
        self.lbl_bank_name.size_hint = (0.7, 1)
        self.lbl_bank_name.halign = 'left'
        self.lbl_bank_name.color = UI_STYLE.M_TEXT_COLOR
        self.lbl_bank_name.text = 'Distortion'

        self.btn_edit_stomp = Button(text='Edit')
        self.btn_edit_stomp.size_hint = (0.1, 1)
        self.btn_edit_stomp.color = UI_STYLE.M_TEXT_COLOR
        self.btn_edit_stomp.background_color = UI_STYLE.M_BUTTON_COLOR
        self.btn_edit_stomp.bind(on_release=self.switch_next)

        status_layout.add_widget(self.btn_bank_bank)
        status_layout.add_widget(self.lbl_bank_name)
        status_layout.add_widget(self.btn_edit_stomp)

        return status_layout

    def switch_bank_select(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'bank'

    def switch_next(self, *args):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'stomp setting'


