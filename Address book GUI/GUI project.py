from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

mainWin=Tk()
mainWin.title("Address Book")
#--------------------------------------
myAddressBook={}

def clear_all():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def update():
    key=name.get()
    if key=="":
        messagebox.showinfo("Error","Name cannot be empty")
    else:
        if key not in myAddressBook.keys():
            book_list.insert(END,key)

            myAddressBook[key]=(address.get(),mobile.get(),email.get(),birthday.get())
            clear_all()

def edit():
    clear_all()
    index=book_list.curselection()
    if index:
        name.insert(0,book_list.get(index))
        
        details=myAddressBook[name.get()]
        
        address.insert(0,details[0])
        
        mobile.insert(0,details[1])
        
        email.insert(0,details[2])
        
        birthday.insert(0,details[3])
        
    else:
        messagebox.showinfo("Error","Select a name")

def delete():
    index=book_list.curselection()
    if index:
        del myAddressBook[book_list.get(index)]
        book_list.delete(index)
        clear_all()
    else:
        messagebox.showinfo("Error","Select a name")

def reset():
    clear_all()
    book_list.delete(0,END)
    myAddressBook.clear()
    book_name.configure(text="My Address Book")

def save():
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        print(myAddressBook,file=fout)
        reset()
    else:
        messagebox.showinfo("Warning","Address Book not saved")

def openFile():
    global myAddressBook
    reset()
    fin=askopenfile(title="Open File")
    if fin:
        myAddressBook=eval(fin.read())
        for key in myAddressBook.keys():
            book_list.insert(END,key)
        book_name.configure(text=os.path.basename(fin.name))
    else:
        messagebox.showinfo("Warning","No address book opened")
#-------------------------------------------------------------   
        
#Designing the main window
#address book name
book_name=Label(mainWin,text="My Address Book",width=35)
book_name.grid(row=0,column=1,pady=10,columnspan=3)

#open button
open_button=Button(mainWin,text="Open",command=openFile)
open_button.grid(row=0,column=3,pady=10)

#Listbox
book_list=Listbox(mainWin,width=30,height=15)
book_list.grid(row=1,column=0,columnspan=3,rowspan=5)

#text field to display contact information
#Name

name_label=Label(mainWin,text="Name")
name_label.grid(row=1,column=3)

name=Entry(mainWin)
name.grid(row=1,column=4,padx=5)

#Address

address_label=Label(mainWin,text="Address")
address_label.grid(row=2,column=3)

address=Entry(mainWin)
address.grid(row=2,column=4,padx=5)

#Mobile Number

mobile_label=Label(mainWin,text="Mobile Number")
mobile_label.grid(row=3,column=3)

mobile=Entry(mainWin)
mobile.grid(row=3,column=4,padx=5)

#Email address

email_label=Label(mainWin,text="Email Address")
email_label.grid(row=4,column=3)

email=Entry(mainWin)
email.grid(row=4,column=4,padx=5)

#Birthday

birthday_label=Label(mainWin,text="Birthday")
birthday_label.grid(row=5,column=3)

birthday=Entry(mainWin)
birthday.grid(row=5,column=4,padx=5)

#buttons
#edit button
edit_button=Button(mainWin,text="Edit",width=10,command=edit)
edit_button.grid(row=6,column=0,pady=10,padx=10)

#Delete button
delete_button=Button(mainWin,text="Delete",width=10,command=delete)
delete_button.grid(row=6,column=1,pady=10,padx=10)

#update/add button
update_button=Button(mainWin,text="Update/Add",width=15,command=update)
update_button.grid(row=6,column=4,pady=10,padx=15)

#save button
save_button=Button(mainWin,text="Save",width=35,command=save)
save_button.grid(row=7,column=1,columnspan=3,pady=10,padx=5)

mainWin.mainloop()





