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


class Door(tk.Toplevel):
    def __init__(self, width, height, widthh, heighth, dwidthh, dheighth):
        super().__init__()

        self.master = game_frame
        self.geometry("%dx%d+%d+%d" % (width, height, widthh, heighth))
        self.resizable(False, False)
        self.opened = False
        self.doorframe = tk.Toplevel()
        self.doorframe.geometry("%dx%d+%d+%d" % (width, height, widthh, heighth))

        self.withdraw()
        self.doorframe.withdraw()


side1 = Door(window_width // 4, window_height, 0, 0, 0, -window_height)
side2 = Door(window_width // 4, window_height, window_width // 4 * 3, 0, window_width // 4 * 3, -window_height)

button1 = tk.Button(window, text="dsfdf", command=lambda: print("df"))
button2 = tk.Button(window, text="dsdfdfsfdf")

button1.pack()
button2.pack()

window.mainloop()
