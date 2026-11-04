import tkinter as tk
from tkinter import ttk
import time
import threading

window = tk.Tk()
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

window.geometry("%dx%d+%d+%d" % (window_width // 2, window_height // 2, window_width // 4, window_height // 4))
window.resizable(False, False)


menu_frame = tk.Frame(window)
menu_frame.pack()

game_frame = tk.Frame()

def change_scene(before, after):
    for i in before:
        if type(i) == Door:
            i.change_visibility(False)
        else:
            i.pack_forget()
    for i in after:
        if type(i) == Door:
            i.change_visibility(True)
        else:
            i.pack()

class Door(tk.Toplevel):
    def __init__(self, width, height, widthh, heighth, dwidthh, dheighth):
        super().__init__()

        self.master = game_frame
        self.geometry("%dx%d+%d+%d" % (width, height, widthh, heighth))
        self.resizable(False, False)
        self.opened = False
        self.doorframe = tk.Toplevel()
        self.doorframe.geometry("%dx%d+%d+%d" % (width, height, dwidthh, dheighth))
        self.withdraw()
        self.doorframe.withdraw()
        self.doorbutton = tk.Button(window, text="block")
        self.lightbutton = tk.Button(window, text="let there be light")

    def change_visibility(self, ahh):
        if ahh:
            self.deiconify()
            self.doorframe.deiconify()
            self.doorbutton.pack()
            self.lightbutton.pack()
        else:
            self.withdraw()
            self.doorframe.withdraw()
            self.doorbutton.pack_forget()
            self.lightbutton.pack_forget()


side1 = Door(window_width // 4, window_height, 0, 0, 0, -window_height)
side2 = Door(window_width // 4, window_height, window_width // 4 * 3, 0, window_width // 4 * 3, -window_height)

button1 = tk.Button(window, text="시작", command=lambda: change_scene(classifryer["menu"], classifryer["game"]))
button2 = tk.Button(window, text="죽기")

button1.pack()
button2.pack()

classifryer = {"menu": [button1, button2], "game": [side1, side2]}

window.mainloop()
