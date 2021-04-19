from logging import setLogRecordFactory
from kivy.app import App
from numpy.lib.function_base import select
from pitch import pitch
from clone import clone
from threading import Lock,Thread
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (320, 240)
pitchObj = pitch()
cloneObj = clone()

class MainWindow(Screen):   
    pass


class PitchWindow(Screen):
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

class CloneWindow(Screen):
    prevSlider = 0
    cloneThread = None
    
    def on_enter(self):
        self.cloneThread = Thread(target=clone.clone, args=(cloneObj, self))
        self.cloneThread.start()

    def pitchChange(self, slider):
        if slider!=self.prevSlider:
            self.prevSlider = slider
    
    def presetChange(self, preset):
        if preset == 1:
            self.prevSlider = -6
        elif preset == 2:
            self.prevSlider = -3
        elif preset == 3:
            self.prevSlider = 4
        elif preset == 4:
            self.prevSlider = 7
    def on_pre_leave(self):   
        cloneObj.stop()

class SeperationWindow(Screen):
    
    def on_enter(self):
        pass

    def on_pre_leave(self):   
        pass
    
        
    
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