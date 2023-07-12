# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from kivy.core.window import Window
from kivy.animation import Animation


from instructions import*
from ruffier import*
from seconds import*
from runner import*
from sits import*




def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.v1 = BoxLayout(orientation = "vertical", spacing = "10sp")
        self.h1 = BoxLayout(pos_hint = {"center_x":0.4}, size_hint = (.7, None), height = "35sp")
        self.h2 = BoxLayout(pos_hint = {"center_x":0.4}, size_hint = (.7, None), height = "35sp")
        self.txt = Label(text = txt_instruction, markup = True)
        self.in_name = TextInput(halign = "left", multiline = False)
        self.in_age = TextInput(halign = "left", multiline = False)
        self.btn = Button(text = "Начать", size_hint = (.3, .15), pos_hint = {"center_x":0.5})
        self.txt_name = Label(text = '[color=#FFFFFF]' + 'Введите имя:' + '[/color]', markup = True)
        self.txt_age = Label(text = "[color=#FFFFFF]" + "Введите возраст:" + '[/color]', markup = True)

        self.btn.on_press = self.next

        self.v1.add_widget(self.txt)

        self.h1.add_widget(self.txt_name)
        self.h1.add_widget(self.in_name)

        self.h2.add_widget(self.txt_age)
        self.h2.add_widget(self.in_age)

        self.v1.add_widget(self.h1)
        self.v1.add_widget(self.h2)
        self.v1.add_widget(self.btn)

        self.add_widget(self.v1)
    def next(self):
        global name
        global age

        name = self.in_name.text
        age = check_int(self.in_age.text)

        if name == "":
            name = ""
            self.in_name.text = str(name)
        else:
            if age == False or age < 7:
                age = 7
                self.in_age.text = str(age)
            else:
                self.manager.transition.direction = "left"
                self.manager.current = "first"
    

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.lbl_sec = Seconds(1, markup = True)
        self.lbl_sec.bind(done = self.finished)

        self.txt1 = Label(text = txt_test1, markup = True)
        self.h1 = BoxLayout(pos_hint = {"center_x":0.5}, size_hint = (.8, None), height = "35sp")
        self.v1 = BoxLayout(orientation = "vertical", spacing = "10sp")
        self.in_result = TextInput(halign = "left", multiline = False, disabled = True)
        self.txt_result = Label(text = "[color=#FFFFFF]" + "Введите результат" + '[/color]', markup = True)
        self.btn = Button(text = "[color=#FFFFFF]" + "Начать" + '[/color]', markup = True, size_hint = (.3, .15), pos_hint = {"center_x":0.5})

        self.btn.on_press = self.next

        self.v1.add_widget(self.txt1)
        self.v1.add_widget(self.lbl_sec)

        self.h1.add_widget(self.txt_result)
        self.h1.add_widget(self.in_result)

        self.v1.add_widget(self.h1)
        self.v1.add_widget(self.btn)

        self.add_widget(self.v1)
    def finished(self, *args):
        self.next_screen = True
        self.in_result.disabled = False
        self.btn.set_disabled(False)
        self.btn.text = "[color=#FFFFFF]" + "Продолжить" + '[/color]'
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global result1

            result1 = check_int(self.in_result.text)

            if result1 == False or result1 == "" or result1 <= 0:
                result1 = 0
                self.in_result.text = str(result1)
            else:
                self.manager.transition.direction = "left"
                self.manager.current = "second"
class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        self.txt = Label(text = txt_sits, markup = True)
        self.h1 = BoxLayout()
        self.run = Runner(total = 30, steptime = 1.5, size_hint = (0.4, 1))
        self.lbl_sits = Sits(30)
        self.run.bind(finished = self.run_finished)
        self.v1 = BoxLayout(orientation = "vertical")
        self.btn = Button(text = "[color=#FFFFFF]" + "Начать" + '[/color]', markup = True, pos_hint = {"center_x":0.5}, size_hint = (.3, .15))

        self.btn.on_press = self.next

        self.h1.add_widget(self.txt)
        self.h1.add_widget(self.v1)
        self.v1.add_widget(self.lbl_sits)
        self.h1.add_widget(self.run)
        self.add_widget(self.h1)
        self.add_widget(self.btn)
    def run_finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.transition.direction = "left"
            self.manager.current = "third"

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0
        self.lbl_sec_text = Label(text = "[color=#FFFFFF]" + "Измерьте пульс" + '[/color]', markup = True)
        self.lbl_sec = Seconds(15, markup = True)
        self.lbl_sec.bind(done = self.finished)
        self.v2 = BoxLayout(orientation = "vertical", size_hint_y = 0.5)
        self.v1 = BoxLayout(orientation = "vertical", spacing = "10sp")
        self.txt = Label(text = txt_test3, markup = True)
        self.h1 = BoxLayout(size_hint = (.7, None), height = "35sp", pos_hint = {"center_x":0.5})
        self.h2 = BoxLayout(size_hint = (.7, None), height = "35sp", pos_hint = {"center_x":0.5})
        self.txt_first = Label(text = "[color=#FFFFFF]" + "Первые 15 сек:" + '[/color]', markup = True)
        self.txt_last = Label(text = "[color=#FFFFFF]" + "Последние 15 сек:" + '[/color]', markup = True)
        self.in_first = TextInput(halign = "left", multiline = False, disabled = True)
        self.in_last = TextInput(halign = "left", multiline = False, disabled = True)
        self.btn = Button(text = "[color=#FFFFFF]" + "Начать" + '[/color]', markup = True, size_hint = (.3, .15), pos_hint = {"center_x":0.5})

        self.btn.on_press = self.next

        self.v2.add_widget(self.txt)
        self.v2.add_widget(self.lbl_sec)
        self.v2.add_widget(self.lbl_sec_text)

        self.v1.add_widget(self.v2)

        self.h1.add_widget(self.txt_first)
        self.h1.add_widget(self.in_first)

        self.h2.add_widget(self.txt_last)
        self.h2.add_widget(self.in_last)

        self.v1.add_widget(self.h1)
        self.v1.add_widget(self.h2)
        self.v1.add_widget(self.btn)

        self.add_widget(self.v1)
    def finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl_sec.restart(30, markup = True)
                self.in_first.set_disabled(False)
                self.lbl_sec_text.text = "[color=#4ef542]" + "Отдыхайте" + '[/color]'
            elif self.stage == 1:
                self.stage = 2
                self.lbl_sec.restart(15, markup = True)
                self.lbl_sec_text.text = "[color=#FFFFFF]" + "Измерьте пульс" + '[/color]'
            elif self.stage == 2:
                self.srage = 3
                self.btn.disabled = False
                self.in_last.set_disabled(False)
                self.btn.text = "[color=#FFFFFF]" + "Завершить" + '[/color]'
                self.next_screen = True
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global result2
            global result3

            result2  = check_int(self.in_first.text)
            result3 = check_int(self.in_last.text)

            if result2 == False or result2 == "" or result2 <= 0:
                result2 = 0
                self.in_first.text = str(result2)
            else:
                if result3 == False or result3 == "" or result3 <= 0:
                    result3 = 0
                    self.in_last.text = str(result3)
                else:
                    self.manager.transition.direction = "left"
                    self.manager.current = "result"
class ResultScr(Screen):
    def __init__(self, **kwargs):
        global result1, result2, result3, age, name
        super().__init__(**kwargs)
        self.v1 = BoxLayout(orientation = "vertical")
        self.txt1 = Label(text = "", markup = True)

        self.v1.add_widget(self.txt1)
        self.add_widget(self.v1)

        self.on_enter = self.before
    def before(self):
            self.txt1.text = "[color=#FFFFFF]" + name + "\n" + test(result1, result2, result3, age) + '[/color]'
        

class Heartcheck(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(InstrScr(name = "instr"))
        sm.add_widget(FirstScr(name = "first"))
        sm.add_widget(SecondScr(name = "second"))
        sm.add_widget(ThirdScr(name = "third"))
        sm.add_widget(ResultScr(name = "result"))

        return sm
    

app = Heartcheck()
app.run()