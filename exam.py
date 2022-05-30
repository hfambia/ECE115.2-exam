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
        self.lapstr = StringVar()
        self.makeWidgets()
        self.prevLapHolder = 0
        self.lapcounter = 1
        self.avglap = []
        self.fastestlap = 99999999
        self.slowestlap = 0
        self.lapcheck = 0
        
    def makeWidgets(self):    
        tree = ttk.Treeview(self)
        tree.pack(side=RIGHT,pady=(24,15),padx=(5,0),fill="both",expand=YES)                     
        self.e = Entry(self)
        timerframe = Frame(self,bg='#425278')
        timerframe.pack(fill="both", pady=(24,5),padx=(0,0),expand=YES)
        timer = Label(timerframe, textvariable=self.timestr,font=('times new roman', 32, 'bold'),bg='#425278',fg='white').pack(anchor = N)
        laplabel = Label(timerframe, text='Current lap time:',font=('segoe UI', 8),bg='#425278',fg='white').pack(side=LEFT,anchor=CENTER,fill=X,expand=YES,padx=(15,0))
        minitimer = Label(timerframe, textvariable=self.lapstr,bg='#425278',fg='white').pack(side=LEFT,anchor=CENTER,fill=X,expand=YES,padx=(0,15))
        self._setTime(self._elapsedtime)
        self._setLapStr(self._elapsedtime)
        extraframe = Frame(self,bg='#425278')
        extraframe.pack(fill='both', expand=1,pady=(0,15),padx=(0,0))
        for r in range(3):
            extraframe.rowconfigure(r, weight=1)
        avgLap = Label(extraframe, text='Average lap time:' ,font=('segoe UI', 8),bg='#425278',fg='white')
        avgLap.grid(column=0,row=0,sticky=W)
        self.avgLapvalue = Label(extraframe, text="00:00:00",bg='#425278',fg='white')
        self.avgLapvalue.grid(column=1,row=0,padx=(20,0))
        fastLap = Label(extraframe, text='Fastest lap time:',font=('segoe UI', 8),bg='#425278',fg='white')
        fastLap.grid(column=0,row=1,sticky=W)
        self.fastLapvalue = Label(extraframe, text="00:00:00",bg='#425278',fg='white')
        self.fastLapvalue.grid(column=1,row=1,padx=(20,0))
        self.fastLapcount = Label(extraframe, text="(#0)",bg='#425278',fg='white')
        self.fastLapcount.grid(column=2,row=1,sticky=W)
        slowLap = Label(extraframe, text='Slowest lap time:',font=('segoe UI', 8),bg='#425278',fg='white')
        slowLap.grid(column=0,row=2,sticky=W)
        self.slowLapvalue = Label(extraframe, text="00:00:00",bg='#425278',fg='white')
        self.slowLapvalue.grid(column=1,row=2,padx=(20,0))
        self.slowLapcount = Label(extraframe, text="(#0)",bg='#425278',fg='white')
        self.slowLapcount.grid(column=2,row=2,sticky=W)      
        tree_scroll = Scrollbar(tree)
        tree_scroll.pack(side=RIGHT, fill=Y)
        self.treeall = ttk.Treeview(tree,yscrollcommand=tree_scroll.set, height=7,style="mystyle.Treeview")
        self.treeall.pack() 
        self.treeall['columns'] = ("#", "Lap Time", "Split Time")
        self.treeall.column("#0", width=0, stretch=NO)
        self.treeall.column("#", anchor=CENTER, width=30)
        self.treeall.column("Lap Time", anchor=CENTER, width=100)
        self.treeall.column("Split Time", anchor=CENTER, width=100)
        self.treeall.heading("0", text="", anchor=W)
        self.treeall.heading("#", text="#", anchor=CENTER)
        self.treeall.heading("Lap Time", text="Lap Time", anchor=CENTER)
        self.treeall.heading("Split Time", text="Split Time", anchor=CENTER)
        self.treeall.pack()
        
    def _update(self): 
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._setLapStr(self._elapsedtime - self.prevLapHolder)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
        
    def _setLapStr(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.lapstr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))  

    def _setLapTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        return '%02d:%02d:%02d' % (minutes, seconds, hseconds)
    
    def Start(self):                                        
        if not self._running:            
            self.lapcheck = 1
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1 
            start.config(state='disable')
            stop.config(state='normal')
            reset.config(state='normal')
            lap.config(state='normal')
            

    def Stop(self):                                    
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
            start.config(state='normal')
            stop.config(state='disable')
         
    def Reset(self):
        self._start = time.time()  
        self.lapcheck = 0
        self._elapsedtime = 0.0
        self.prevLapHolder = 0
        self.lapcounter = 1
        self.avglap = []
        self.fastestlap = 99999999
        self.slowestlap = 0
        self.laps = []   
        self._setTime(self._elapsedtime)
        self._setLapStr(self._elapsedtime)
        self.after_cancel(self._timer)            
        self._elapsedtime = 0.0
        self.treeall.delete(*self.treeall.get_children())
        lap.config(state='disable')
        start.config(state='normal')
        stop.config(state='disable')
        reset.config(state='disable')
        self.avgLapvalue.config(text="00:00:00")
        self.avgLapvalue.config(text="00:00:00")
        self.fastLapvalue.config(text="00:00:00")
        self.fastLapcount.config(text="(#0)")
        self.slowLapvalue.config(text="00:00:00")
        self.slowLapcount.config(text="(#0)")
        self._running = 0
    
    def Lap(self):
       tempo = self._elapsedtime - self.prevLapHolder
       if self._running or self.lapcheck ==1:
           if not self._running: self.lapcheck = 0, lap.config(state='disable')
           self.avglap.append(tempo)
           self.avgLapvalue.config(text=(self._setLapTime((sum(self.avglap))/self.lapcounter)))
           if tempo < self.fastestlap:
                self.fastestlap = tempo
                self.fastLapvalue.config(text=self._setLapTime(tempo))
                self.fastLapcount.config(text=("(#" + str(self.lapcounter) + ")"))
           if tempo > self.slowestlap:
                 self.slowestlap = tempo
                 self.slowLapvalue.config(text=self._setLapTime(tempo))
                 self.slowLapcount.config(text=("(#" + str(self.lapcounter) + ")"))
           self.laps.append(self._setLapTime(tempo))
           self.treeall.insert(parent='',index=0,text='', values=(self.lapcounter,self._setLapTime(tempo),self._setLapTime(self._elapsedtime)))
           self.lapcounter += 1
           self.prevLapHolder = self._elapsedtime
           self.treeall.config(background='black')
           


global lap
global start
global stop
global reset

root = Tk()
style = ttk.Style(root)
style.theme_use("vista")
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('segoe UI', 11)) 
style.configure("mystyle.Treeview.Heading", font=('segoe UI', 13)) 
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
root.title('Exam')
root.geometry("500x280")
root.resizable(False, False)
root.wm_attributes("-topmost", 1)
root.config(bg ='#32394a')

sw = StopWatch(root)
sw.config(bg = '#32394a')
sw.pack()
lap = Button(root, text='Lap',bg='#425278',
fg='white', activebackground='#8e9cbf', activeforeground='white',command=sw.Lap, state='disable',font=('segoe UI', 12),relief=SOLID,borderwidth=1)
lap.pack(side=LEFT,fill=BOTH, expand=YES, anchor=S,padx=(29,4),pady=(0,29))
start = Button(root, text='Start',bg='#425278',
fg='white', activebackground='#8e9cbf', activeforeground='white',command=sw.Start,font=('segoe UI', 12),relief=SOLID,borderwidth=1)
start.pack(side=LEFT,fill=BOTH, expand=YES, anchor=S,padx=4,pady=(0,29))
stop = Button(root, text='Stop',bg='#425278',
fg='white', activebackground='#8e9cbf', activeforeground='white',command=sw.Stop, state='disable',font=('segoe UI', 12),relief=SOLID,borderwidth=1)
stop.pack(side=LEFT,fill=BOTH, expand=YES, anchor=S,padx=(4),pady=(0,29))
reset = Button(root, text='Reset',bg='#425278',
fg='white', activebackground='#8e9cbf', activeforeground='white', command=sw.Reset, state='disable',font=('segoe UI', 12),relief=SOLID,borderwidth=1)
reset.pack(side=LEFT,fill=BOTH, expand=YES, anchor=S,padx=(4,30),pady=(0,29))
root.mainloop()
    
    
    
