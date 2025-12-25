from tkinter import *

def click(val):
    e.insert(END,val)

def clear():
    e.delete(0,END)

def calc():
    result = eval(e.get())
    clear()
    e.insert(0,result)

root = Tk()
root.title("Calculator")

e = Entry(root,width=20)
e.grid(row=0,column=0,columnspan=4)

b = ["7","8","9","+","4","5","6","-","1","2","3","*","0","C","=","/"]
r=c=0

for i in b:
    if i=="C":
        Button(root,text=i,command=clear).grid(row=r+1,column=c)
    elif i=="=":
        Button(root,text=i,command=calc).grid(row=r+1,column=c)
    else:
        Button(root,text=i,command=lambda x=i:click(x)).grid(row=r+1,column=c)
    c+=1
    if c>3:
        c=0
        r+=1

root.mainloop()
