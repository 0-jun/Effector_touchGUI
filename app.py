import sys

from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'fullscreen', '0')

from multiprocessing import freeze_support

from View import home_view
from View import stomp_set_view


class App(App):
    def build(self):
        #self.usb_model = usbManager.UsbManager()
       # AppSetting.SCREEN_WIDTH = self.primaryScreen().size().width()
       # AppSetting.SCREEN_HEIGHT = self.primaryScreen().size().height()
       # self.main_controller = UsbController.UsbController(self.usb_model)
        root = ScreenManager()
        root.add_widget(home_view.HomeView(name='Screen home'))
        root.add_widget(stomp_set_view.StompSettingView(name='Screen stomp setting'))

        return root


if __name__ == "__main__":
    freeze_support()
    App().run()
