from tkinter import *
import time

class StopWatch(Frame):                                                           
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._elapsedtime = 0.0
        self.timestr = StringVar()
        self.makeWidgets()
        
    def makeWidgets(self):                         
        self.e = Entry(self)
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=4, padx=2)
        l2 = Label(self, text='Laps')
        l2.pack(fill=X, expand=NO, pady=4, padx=90)
        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.m = Listbox(self,selectmode=EXTENDED, height = 5, yscrollcommand=scrollbar.set)
        self.m.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=2)
        scrollbar.config(command=self.m.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        
    def _update(self): 
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
       
    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def Start(self):                                          
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._running = 1
        
        
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

    
if __name__ == '__main__':
    main()
    
