__version__ = '0.1'
from kivy.app import App
from kivy.uix.button import Button
# import numpy as np
# import PIL
  
class Hello(App):
    def build(self):
        # foo = np.array([1, 2, 3])
        btn = Button(text='Python Image Compression in Android!')
        return  btn
  
Hello().run()
