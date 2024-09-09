from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Imgaes in Tkinder')

root.geometry('340x440')

my_img1 = ImageTk.PhotoImage(Image.open("images/Stargazing.jpg").resize((200, 200)))

my_img2 = ImageTk.PhotoImage(Image.open("images/img1.jpg").resize((200, 200)))
my_img3 = ImageTk.PhotoImage(Image.open("images/img2.jpg").resize((200, 200)))
my_img4 = ImageTk.PhotoImage(Image.open("images/img3.jpg").resize((200, 200)))
my_img5 = ImageTk.PhotoImage(Image.open("images/Stargazing.jpg").resize((200, 200)))

my_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image = my_img1)
# my_label.resize((250, 250),Image.ANTIALIAS)
my_label.grid(row=0, column=0, columnspan=3)
def back():
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
def forward(image_no):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label=Label(image=my_list[image_no-1])
    button_forward=Button(root,text=">>",command=lambda :forward(image_no+1))
    button_back = Button(root, text=">>", command=lambda: back(image_no - 1))
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)




button_back = Button(root, text="<<",command=lambda :back())
button_exit = Button(root, text="Quit", command=root.quit)
button_forward = Button(root, text=">>",command=lambda :forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()
