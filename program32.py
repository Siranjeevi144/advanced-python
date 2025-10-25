from tkinter import *

root=Tk()
root.title("Login page")
root.geometry("700x500")

l=Label(root,text="user name")
l.pack()

e=Entry(root)
e.pack()

b=Button(root,text="login")
b.pack()

root.mainloop()
