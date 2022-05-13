from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition

Builder.load_file('View/kv_file/stomp_set_view.kv')


class StompSettingView(Screen):
    def __init__(self, **kwargs):
        super(StompSettingView, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Create buttons with a custom text
        prev = Button(text='Previous')

        # Bind to 'on_release' events of Buttons
        prev.bind(on_release=self.switch_prev)

        layout.add_widget(Label(text='stmop', font_size=50))
        layout.add_widget(prev)

        self.add_widget(layout)

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

