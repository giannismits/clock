from time import strftime
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock


class ClockApp(App):
    sw_seconds = 0
    sw = False

    def on_start(self):
        Clock.schedule_interval(self.update, 0.016)

    def update(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        if self.sw:
            self.sw_seconds += nap
            minutes,  seconds = divmod(self.sw_seconds, 60)
            self.root.ids.stopwatch.text = (
                '%02d:%02d.[size=40]%02d[/size]' %
                (int(minutes), int(seconds),
                int(seconds * 100 % 100)))

    def start_stop(self):
        self.root.ids.start_stop.text = ('Stop'
            if not self.sw else 'Start')
        self.sw = not self.sw



    def reset(self):
        if not self.sw:
            self.sw_seconds = 0
            self.root.ids.stopwatch.text = '00:00.[size=40]00[/size]'


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101E16')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Bold.ttf',
                       fn_bold='Roboto-Regular.ttf')
    ClockApp().run()
