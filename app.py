from kivy.app import App
from pitch import pitch
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass
    def pitchChange(self, slider):
        if(slider != 0.0):
            pitch.modulate(self, slider)
        
    
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("modulator.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()