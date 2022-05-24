from tkinter import *
import time

class StopWatch(Frame):                                                           
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
            
def main():
    root = Tk()
    root.title('Exam')
    root.geometry("250x200")
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    sw = StopWatch(root)
    sw.pack(side=TOP)
    Button(root, text='Lap').pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Start').pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Stop').pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Reset').pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Quit').pack(side=LEFT,fill=X, expand=YES, anchor=S)
    root.mainloop()
