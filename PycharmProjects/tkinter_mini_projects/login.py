import tkinter
from tkinter import messagebox

# tkinter._test()
window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')


def login():
    username = "mallika"
    password = "1234"
    if username_entry.get()==username and password_entry.get()==password:
            messagebox.showinfo(title="Login Success",message="You Successfully login")
    else:
        print("Invalid Login")



frame = tkinter.Frame(bg='#333333')

#Creating widgets
login_lable = tkinter.Label(frame, text="Login", bg='#333333', fg='#ff3399', font=("Arial", 30))
username_lable = tkinter.Label(frame, text="Userame", bg='#333333', fg='#ffffff', font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show='*', font=("Arial", 16))
password_lable = tkinter.Label(frame, text="password", bg='#333333', fg='#ffffff', font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg='#ff3399', fg='#ffffff', font=("Arial", 16), command=login)

frame.pack()

#placing widgets on the screen
login_lable.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_lable.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_lable.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

window.mainloop()
