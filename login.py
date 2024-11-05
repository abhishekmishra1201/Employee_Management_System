from customtkinter import *
from PIL import Image
from tkinter import messagebox
# import  ems

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error',"All fields are required")
    elif usernameEntry.get()=='Abhishek' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is Successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong Credentials')



root=CTk()


root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('colleagues-working-together-project_74855-6308.jpg'),size=(930,478))

imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text="Employee Management System",bg_color='#ffffff',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=20,y=100)


usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordEntry.place(x=50,y=200)


loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=70,y=250)

root.mainloop()




