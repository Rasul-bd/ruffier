# напиши модуль для реализации секундомера
from kivy.properties import BooleanProperty
from kivy.uix.label import Label
from kivy.clock import Clock

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = "[color=#FFFFFF]" + "Прошло секунд: " + str(self.current) + "[/color]"
        super().__init__(text=my_text, markup = True)
        self.done = False
    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = "[color=#FFFFFF]" + "Прошло секунд: " + str(self.current) + '[/color]'
        self.start()
    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = "[color=#FFFFFF]" + "Прошло секунд: " + str(self.current) + '[/color]'
        if self.current >= self.total:
            self.done = True
            return False