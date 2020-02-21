from tkinter import *
from tkinter.filedialog import askopenfilename
import hashlib
import datetime

class hashEncrypt:
    def __init__(self):
        self.win = Tk()
        self.win["bg"] = '#D3D3D3'
        self.win.geometry("600x400")
        self.path = ''
        self.encrypted = False
        
        self.label1 = Label(self.win,text="Select file",width = 100)
        self.label1.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.label1["bg"] = '#D3D3D3'
        
        self.button1 = Button(self.win, text="Select", width=10, height=5,command=self.select)
        self.button1.place(relx=0.25, rely=0.7, anchor=CENTER)
        self.button1["bg"] = '#9999ff'
        
        self.button2 = Button(self.win, text="Hash", width=10,height=5, command=self.encrypt)
        self.button2.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.button2["bg"] = '#9999ff'
        
        self.button3 = Button(self.win, text="Lock", width=10, height=5,command=self.save)
        self.button3["bg"] = '#9999ff'
        self.button3.place(relx=0.75, rely=0.7, anchor=CENTER)
    
    def select(self):
        self.path = askopenfilename()
        self.label1 = Label(self.win,text="File selected")
        self.label1.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    def encrypt(self):
        if not self.path == '':
            with open(self.path, 'rb') as f:
                self.hash = hashlib.sha256(f.read()).hexdigest()
    
            self.encrypted = True
            self.label1 = Label(self.win,text="File hashed")
            self.label1.place(relx=0.5, rely=0.25, anchor=CENTER)
                
    def save(self):
        if self.encrypted == True:
            f = open('hashed.txt','w')
            for i in range(len(self.path)):
                if self.path[i] == "/":
                    temp = i
                    
            self.path = self.path[temp+1:len(self.path)]
            
            f.write(self.hash)
            f.write("\n"+str(self.path))
            f.write("\n"+str(datetime.datetime.now()))
            f.close
            self.label1 = Label(self.win,text="File saved")
            self.label1.place(relx=0.5, rely=0.25, anchor=CENTER)
            
test = hashEncrypt()


