from tkinter import *
import sqlite3
root=Tk()
root.title("login")
root.geometry('400x400')
root.config(bg="antiquewhite")
#user login
Label(root,text="userId:",bg="antiquewhite").place(relx=.3,rely=.3,anchor=CENTER)
e1=Entry(root,width=20).place(relx=.6,rely=.3,anchor=CENTER)
Label(root,text="password:",bg="antiquewhite").place(relx=.3,rely=.4,anchor=CENTER)
e2=Entry(root,width=20).place(relx=.6,rely=.4,anchor=CENTER)
bf=Button(root,text="forget password").place(relx=.4,rely=.5,anchor=CENTER)
bl=Button(root,text="  login   ").place(relx=.6,rely=.5,anchor=CENTER)
bc=Button(root,text="create new account").place(relx=.5,rely=.6,anchor=CENTER)
root.mainloop()
