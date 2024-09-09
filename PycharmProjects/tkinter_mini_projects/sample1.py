from tkinter import *

top = Tk()
top.geometry("350x300")
top.title('Simple Application')
top.config(bg='#ffffff')
top.resizable(width=False, height=False)

a=0
d=0
c=0
def one():
    global a
    a=a+1
    msg = Message(top, text=a,fg="blue").place(x=210,y=60)
def two():
    global d
    d=d+2
    msg = Message(top,text=d,fg="blue").place(x=210,y=100)
def three():
    global c
    c=c+3
    msg = Message(top,text=c,fg="blue").place(x=210,y=140)
def ref():
    global a
    global d
    global c
    a=0
    d=0
    c=0
    msg = Message(top, text=a,fg="blue").place(x=210, y=60)
    msg = Message(top, text=d,fg="blue").place(x=210, y=100)
    msg = Message(top, text=c,fg="blue").place(x=210, y=140)


b = Button(top,text ="Button 1",command = one,fg="blue",padx=11).place(x=105,y=60)
g = Button(top,text = "Button 2",command = two, fg="blue",padx=11).place(x=105,y=100)
e = Button(top,text = "Button 3",command = three, fg="blue",padx=11).place(x=105,y=140)

f = Button(top,text = "Refresh",command = ref,fg="blue",padx=38).place(x=105,y=200)

#l = Label(top, text = "Name").place(x = 180,y = 140)
top.mainloop()