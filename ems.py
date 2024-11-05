from tkinter import ttk, messagebox

from PIL import Image
from customtkinter import *
from customtkinter import CTkFrame

import data_base


#Function

def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the records?')
    if result:
        data_base.deleteall_records()
    else:
        pass


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')



def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    else:
        searched_data=data_base.search(searchBox.get(),searchEntry.get())
        # print(searched_data)
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)




def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Selected data to delete')
    else:
        data_base.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is Deleted')



def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        data_base.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('success','Data will updated')


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])




def treeview_data():
    employees = data_base.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)


def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required ')
    elif data_base.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error','Invalid Id format. Use "EMP" followed by a number (e.g., "EMP" ).')

    else:
        data_base.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        messagebox.showinfo('success','Data is added')



#GUI

window=CTk()

window.geometry('1000x580+100+100')
window.resizable(False,False)

window.configure(fg_color='#161C30')

logo=CTkImage(Image.open('untitled design.png'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)



window.title('Employee Management System')


leftFrame=CTkFrame(window,fg_color='#161C30')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20,pady=15)

idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)


nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1)


phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

phoneEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
phoneEntry.grid(row=3, column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

role_options=['Web Developer','Cloud Architech','Technical Writer','Network Engineer','DevOps','Data Scientist','Business Analyst','IT Consultant','Ui/Ux Designer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',18,'bold'),state='readonly')
roleBox.grid(row=4,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',18,'bold'),state='readonly')
genderBox.grid(row=5,column=1)
genderBox.set(gender_options[0])


salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=6,column=0,padx=20,pady=15,sticky='w')

salaryEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=6, column=1)


rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Phone','Role','Gender','Salary']

searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)


showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')


tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=140)


style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowheight=30,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview())
scrollbar.grid(row=0,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda : clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,padx=5)


treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()