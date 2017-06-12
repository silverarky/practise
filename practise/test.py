#-*- coding:utf-8 -*-
import tkinter as tk
class APP:
    def __init__(self,master):
        frame=tk.Frame(root)
        frame.grid(row=0,column=0,sticky="W")
        
        self.hi_kk=tk.Buttom(frame,text="k")
root=tk.Tk()
app=APP(root)
root.mainloop()