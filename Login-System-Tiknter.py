

from tkinter import *

win = Tk()

win.geometry('400x260')

def login():
	if username.get() == 'user' and password.get() == '123':
		print('logedin')
	else:
		print('password is wrong')

# create titel
titel = Label(win, text = 'Login', bd =0, font = ('sans-serif', 25))
titel.place(x = 20, y = 20)

# create entrys
username = Entry(win, bd = 0, font = ('sans-serif', 20))
username.place(x = 20, y = 80)

password = Entry(win, bd = 0, font = ('sans-serif', 20))
password.place(x = 20, y = 130)

# create bt
bt = Button(win, text = "Login Now", bd = 0, bg="#74b9ff", font = ('sans-serif', 20), command = login)
bt.place(x = 20, y = 170)

win.mainloop()