
import AppConstant

from View import bank_view
from View import home_view
from View import stomp_set_view

from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'fullscreen', '0')


class App(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(home_view.HomeView(bank_num='A1', name=AppConstant.SCREEN_HOME))
        root.add_widget(bank_view.BankView(name=AppConstant.SCREEN_BANK_SEL))
        root.add_widget(stomp_set_view.StompSettingView(name=AppConstant.SCREEN_STOMP_SET))
        root.current = AppConstant.SCREEN_HOME
        return root


if __name__ == "__main__":
    App().run()
