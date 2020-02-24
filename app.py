import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label



class modulator(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    modulator().run()
