from tkinter import *

root = Tk()

root.title("INHERITANCE")
root.geometry("400x500")

Label1 = Label(root,text="Name")
Label1.place(relx=0.2,rely=0.4,anchor=CENTER)

user_name = Entry(root)
user_name.place(relx=0.6,rely=0.4,anchor=CENTER)

Label2 = Label(root,text="Email Id")
Label2.place(relx=0.2,rely=0.6,anchor=CENTER)

user_id = Entry(root)
user_name.place(relx=0.6,rely=0.6,anchor=CENTER)

Button = Button(root,text="ADD ID",command=Save)
Button.place(relx=0.5,rely=0.8,anchor=CENTER)

label_1_2 = Label(root,text="")
label_1_2.place(relx=0.8,rely=0.9,anchor=CENTER)

label_2_1 = Label(root,text="")
label_2_1.place(relx=0.8,rely=0.10,anchor=CENTER)

user_name_var = user_name.get() 
user_id_var = user_id.get()

def Save():
    label_1_2 = Label(root,text=user_name_var)
    label_2_1 = Label(root,text=user_id_var)
    
Button = Button(root,text="ADD ID",command=Save)
Button.place(relx=0.5,rely=0.8,anchor=CENTER)