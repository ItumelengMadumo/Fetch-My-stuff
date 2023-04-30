from tkinter import*
from functools import partial

def validateRegistration(Name_Surname ,username, password):
    print("Name Surname :", Name_Surname.get())
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Fecth My Stuff Registration Page')

#Name_Surname label and password entry box
Name_SurnameLabel = Label(tkWindow,text="Name_Surname").grid(row=1, column=0)  
Name_Surname = StringVar()
Name_Surname = Entry(tkWindow, textvariable=Name_Surname).grid(row=1, column=1)  

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  



validateRegistration = partial(validateRegistration, username, password, Name_Surname)

#Register button
RegisterButton = Button(tkWindow, text="Register", command=validateRegistration).grid(row=4, column=0)  

tkWindow.mainloop()