from tkinter import *
from tkinter import ttk
import time

class StopWatch(Frame):                                                           
    def __init__(self, parent=None):        
        Frame.__init__(self, parent)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.laps = []
        self.timestr = StringVar()
        self.makeWidgets()
        self.prevLapHolder = 0
        self.lapcounter = 1
        
    def makeWidgets(self):                         
        self.e = Entry(self)
        TimerText = Label(self, text='Time')
        TimerText.pack(fill=X, expand=NO, padx=80)
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, padx=2)
        
        
        
        tree = ttk.Treeview(self,height=3)
        tree.pack()
        tree_scroll = Scrollbar(tree)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.treeall = ttk.Treeview(tree,yscrollcommand=tree_scroll.set)
        self.treeall.pack() 
        
        self.treeall['columns'] = ("#", "Lap Time", "Split Time")
        
        self.treeall.column("#0", width=0, stretch=NO)
        self.treeall.column("#", anchor=CENTER, width=15)
        self.treeall.column("Lap Time", anchor=CENTER, width=80)
        self.treeall.column("Split Time", anchor=CENTER, width=80)
        
        self.treeall.heading("0", text="", anchor=W)
        self.treeall.heading("#", text="#", anchor=CENTER)
        self.treeall.heading("Lap Time", text="Lap Time", anchor=CENTER)
        self.treeall.heading("Split Time", text="Split Time", anchor=CENTER)
        self.treeall.pack()
        
        

        
        
        
    def _update(self): 
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
        

    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def _setLapTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)            
        return '%02d:%02d:%02d' % (minutes, seconds, hseconds)
    
    
    def Start(self):                                          
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1 
    
    def Stop(self):                                    
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
         
    def Reset(self):
        self._start = time.time()         
        self._elapsedtime = 0.0
        self.prevLapHolder = 0
        self.lapcounter = 1
        self.laps = []   
        self._setTime(self._elapsedtime)
        self.after_cancel(self._timer)            
        self._elapsedtime = 0.0
        self.treeall.delete(*self.treeall.get_children())
        self._running = 0
    
    def Lap(self):
       tempo = self._elapsedtime - self.prevLapHolder
       if self._running:
           self.laps.append(self._setLapTime(tempo))
           self.treeall.insert(parent='',index=0,text='', values=(self.lapcounter,self._setLapTime(tempo),self._setLapTime(self._elapsedtime)))
           self.lapcounter += 1
           self.prevLapHolder = self._elapsedtime
      
        
def main():
    root = Tk()
    root.title('Exam')
    root.geometry("250x300")
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    sw = StopWatch(root)
    sw.pack(side=TOP)
    Button(root, text='Lap',command=sw.Lap).pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Start',command=sw.Start).pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Stop',command=sw.Stop).pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Reset', command=sw.Reset).pack(side=LEFT,fill=X, expand=YES, anchor=S)
    Button(root, text='Quit',command=root.destroy).pack(side=LEFT,fill=X, expand=YES, anchor=S)
    root.mainloop()

    
if __name__ == '__main__':
    main()
