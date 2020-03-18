from kivy.app import App
from pitch import pitch
from threading import Lock,Thread
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

pitchObj = pitch()

class MainWindow(Screen):   
    pass


class SecondWindow(Screen):
    prevSlider = 0
    pitchThread = None
        

    def on_enter(self):
        self.pitchThread = Thread(target=pitch.modulate, args=(pitchObj,self))
        self.pitchThread.start()

    def on_pre_leave(self): 
        pitchObj.stop()
    
    def pitchChange(self, slider):
        if slider!=self.prevSlider:
            self.prevSlider = slider
        
    
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("modulator.kv")


class Modulator(App):
    def on_stop(self):
        pitchObj.stop()

    def build(self):
        return kv


if __name__ == "__main__":
    Modulator().run()