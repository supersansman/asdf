import tkinter as tk
from tkinter import ttk
import time
import threading

window = tk.Tk()
window_width = window.winfo_screenwidth() // 2
window_height = window.winfo_screenheight() // 2

window.geometry("%dx%d+%d+%d" % (window_width, window_height, window_width // 2, window_height // 2))
window.resizable(False, False)

window.mainloop()
