
from tkinter import * 
from tkinter import filedialog

def loc_browser():
    root = Tk()
    root.filename = filedialog.askopenfilename(title='Select New Backup Location')
    root.destroy()
    return root.filename
# print(loc_browser())