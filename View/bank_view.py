from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition

from Model import UI_STYLE


class BankView(Screen):

    def __init__(self, **kwargs):
        super(BankView, self).__init__(**kwargs)

        top_layout = BoxLayout(orientation='vertical')

        btn_back = Button(text='Back')
        btn_back.color = UI_STYLE.M_TEXT_COLOR
        btn_back.background_color = UI_STYLE.M_BUTTON_COLOR
        btn_back.bind(on_release=self.switch_back)

        main_bank_layout = GridLayout()
        main_bank_layout.cols = 5
        main_bank_layout.rows = 5

        btn_bank_list = list()
        for i in range(0, 10):
            btn_bank_list.append(Button(text='A' + str(i)))
            btn_bank_list[-1].color = UI_STYLE.M_TEXT_COLOR
            btn_bank_list[-1].background_color = UI_STYLE.M_BUTTON_COLOR

        for i in range(0, 10):
            main_bank_layout.add_widget(btn_bank_list[i])

        top_layout.add_widget(btn_back)
        top_layout.add_widget(main_bank_layout)
        self.add_widget(top_layout)

    def switch_back(self, *args):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'home'


