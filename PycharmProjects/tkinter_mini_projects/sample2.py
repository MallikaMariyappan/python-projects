from tkinter import *
root=Tk()


def myClick():
    label=Label(root,text="I Clicked")
    label.pack()
mylabel=Label(root,text="Hello world")
mylabel2=Label(root,text="Welcome")
button=Button(root,text="click me!!!",command=myClick,padx=20,pady=30,fg="blue",bg="yellow")

# mylabel.grid(row=0,column=0)
# mylabel2.grid(row=1,column=0)
button.pack()


root.mainloop()