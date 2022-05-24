from tkinter import *
import time

class StopWatch(Frame):                                                           
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
            
def main():
    root = Tk()
    root.wm_attributes("-topmost", 1)
    sw = StopWatch(root)
    sw.pack(side=TOP)
    Button(root, text='Lap').pack(side=LEFT)
    Button(root, text='Start').pack(side=LEFT)
    Button(root, text='Stop').pack(side=LEFT)
    Button(root, text='Reset').pack(side=LEFT)
    Button(root, text='Quit').pack(side=LEFT)    
    root.mainloop()

if __name__ == '__main__':
    main()