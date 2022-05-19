from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition

import AppConstant
from Model import UI_STYLE


class BankView(Screen):

    def __init__(self, **kwargs):
        super(BankView, self).__init__(**kwargs)

        top_layout = BoxLayout(orientation='vertical')

        main_bank_layout = GridLayout()
        main_bank_layout.cols = 4
        main_bank_layout.rows = 2

        btn_bank_list = list()
        for i in range(0, 8):
            btn_bank_list.append(Button(text='A' + str(i)))
            btn_bank_list[-1].color = UI_STYLE.M_TEXT_COLOR
            btn_bank_list[-1].background_color = UI_STYLE.M_BUTTON_COLOR
            btn_bank_list[-1].bind(on_release=self.event_select_bank)

        for i in range(0, 8):
            main_bank_layout.add_widget(btn_bank_list[i])

        top_layout.add_widget(main_bank_layout)
        self.add_widget(top_layout)

    def event_select_bank(self, *args):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.get_screen(AppConstant.SCREEN_HOME).btn_bank_sel.text = args[0].text
        self.manager.current = AppConstant.SCREEN_HOME


