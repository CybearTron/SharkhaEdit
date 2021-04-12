from tkinter import *
import os
import tkinter.messagebox
import tkinter.filedialog as filedialog
#Imports the frickin  modules
titley="Sharkha Edit"
#The Title variable I will use again and agan

root=Tk()
#The Root Window
root.geometry("800x600")


root.iconbitmap('D:\practice snek\SharkhaEdit\icon.ico')

#Sizing
root.minsize(height=560)
root.title(titley)
#title
ribbon=Frame(root,width="10",height="5",bg="#434C5E")
ribbon.pack(side=TOP)
tekstfrem=Frame(root,width="200",height="500",bg="#2E3440")
tekstfrem.pack(fill=BOTH,side=LEFT)



lebel=Label(ribbon,bg="#3B4252",fg="#D8DEE9")
lebel.pack()
scol=Scrollbar(tekstfrem)
scol.pack(side=RIGHT,fill=Y)

tekst=Text(tekstfrem,yscrollcommand=scol.set,bg="#4C566A",fg="white",wrap=WORD)
tekst.pack(fill=BOTH)

scol.config(command=tekst.yview)


def sev():
    global tekst
    tex=tekst.get("1.0","end-1c")
    sevloc=filedialog.asksaveasfilename()
    fil=open(sevloc,"w+")
    fil.write(tex)
    fil.close()
def op():
    global tekst
    tex=tekst.get("1.0","end-1c")
    new=filedialog.askopenfilename()
    fil=open(new,"r")
    tekst.delete("1.0","end")
    tekst.insert("1.0",fil.read())
    lebel.configure(text=new)
    fil.close()
def new():
    global tekst
    tex=tekst.get("1.0","end-1c")
    neu=filedialog.asksaveasfilename()
    
    
    tekst.delete("1.0","end")
    
menumain=Menu(ribbon)
menumain.add_cascade(label="File",menu)
menumain.add_command(label="Save?",command=sev)
menumain.add_command(label="Open?",command=op)
menumain.add_command(label="New?",command=new)

root.config(menu=menumain,bg="#3B4252")
root.mainloop()