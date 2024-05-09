from tkinter import *


class MM(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)


window = MM()
window.mainloop()
