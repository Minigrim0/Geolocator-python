from tkinter import filedialog
from tkinter import *

def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    return filename
