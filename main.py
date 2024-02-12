import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
from EncryptAndDecrypt import *
from Hash import *

# Create a new Tkinter instance
root = Tk()
root.title("Secure Password Manager - John Doe")
root.geometry("400x400")

# Use the new person's username variable
john_username_var = StringVar()
john_password_var = StringVar()

# ASKING USERNAME AND PASSWORD
label1 = Label(root, text="Username: ")
label1.place(x=10, y=150)
username = Entry(root, width=50, borderwidth=5, textvariable=john_username_var)
username.place(x=80, y=150)

label2 = Label(root, text="Password: ")
label2.place(x=10, y=180)
password = Entry(root, width=50, borderwidth=5, textvariable=john_password_var)
password.place(x=80, y=180)

uk = None

# REGISTER BUTTON
def register():
    global top
    top = Toplevel()
    top.title("Registration form - John Doe")
    top.geometry("550x350")

    # Use the new person's username for the database
    usrinfo = sqlite3.connect("john_doe_info.db")
    u = usrinfo.cursor()
    u.execute("CREATE TABLE IF NOT EXISTS userinfo( FName Text, SName Text,email Text, Phone NUMERIC,usernameText,PasswordHash,UniqueKey)")
    usrinfo.commit()
    usrinfo.close()

    def create_account():
        global john_username
        john_username = u_name.get()

        if john_username == "":
            messagebox.showerror("Warning!", "Enter username")

        elif email.get() == "":
            messagebox.showerror("Warning!", "Enter E-mail")

        elif f_name.get() == "":
            messagebox.showerror("Warning!", "Enter your first name")

        elif l_name.get() == "":
            messagebox.showerror("Warning!", "Enter your last name")

        elif ph_num.get() == "":
            messagebox.showerror("Warning!", "Enter phone number")

        elif n_pass.get() == "":
            messagebox.showerror("Warning!", "Enter New Password")

        else:
            acc = sqlite3.connect(f"{john_username}.db")
            a = acc.cursor()
            a.execute(f"CREATE TABLE IF NOT EXISTS passwords( Domain Text, username Text,email Text, passwordEncrypt, description Text)")
            acc.commit()
            acc.close()

        fname = f_name.get()
        lname = l_name.get()
        mal = email.get()
        phone = ph_num.get()
        new_pass = n_pass.get()
        hash_pass = creatingHash(new_pass)
        generateUniqueKey()
        uniqueKey = getUniqueKey().decode()
        destroyUniqueKey()

        usrinfo = sqlite3.connect("john_doe_info.db")
        u = usrinfo.cursor()
        u.execute("INSERT INTO userinfo VALUES('"+fname+"','"+lname+"','"+mal+"','"+phone+"','"+john_username+"','"+hash_pass+"','"+uniqueKey+"')")
        messagebox.showinfo("Information", "Successfully Inserted!")
        top.destroy()
        usrinfo.commit()
        usrinfo.close()

    label3 = Label(top, text="First Name: ")
    label3.place(x=70, y=50)
    f_name = Entry(top, width=50, borderwidth=5)
    f_name.place(x=180, y=50)
    label4 = Label(top, text="Last Name: ")
    label4.place(x=70, y=80)
    l_name = Entry(top, width=50, borderwidth=5)
    l_name.place(x=180, y=80)
    label5 = Label(top, text="E-mail: ")
    label5.place(x=70, y=110)
    email = Entry(top, width=50, borderwidth=5)
    email.place(x=180, y=110)
    label6 = Label(top, text="Ph-Num: ")
    label6.place(x=70, y=140)
    ph_num = Entry(top, width=50, borderwidth=5)
    ph_num.place(x=180, y=140)
    label7 = Label(top, text="Username: ")
    label7.place(x=70, y=170)
    u_name = Entry(top, width=50, borderwidth=5)
    u_name.place(x=180, y=170)
    label8 = Label(top, text="New Password: ")
    label8.place(x=70, y=200)
    n_pass = Entry(top, width=50, borderwidth=5)
    n_pass.place(x=180, y=200)
    btn3 = Button(top, text="Create Account", command=create_account)
    btn3.place(x=255, y=250)

# LOGIN
def log_in():
    global john_username_var
    global john_password_var
    u = john_username_var.get()
    if not os.path.isfile(f'{u}.db'):
        messagebox.showinfo("Warning!", "No Account Found! Create an Account")
        return
    else:
        usrinfo = sqlite3.connect("john_doe_info.db")
        c = usrinfo.cursor()
        try:
            c.execute(f'''SELECT PasswordHash,UniqueKey FROM userinfo WHERE usernameText="{u}"''')
            data = c.fetchall()[0]
            global uk
            uk = data[1].encode()
            if not verifyingHash(john_password_var.get(), data[0]):
                messagebox.showinfo("Warning!", "Incorrect Username or Password")
                return
        except:
            messagebox.showinfo("Warning!", "Incorrect Username or Password")
            return
        usrinfo.commit()
        usrinfo.close()

    bottom = Toplevel()
    bottom.title("Passwords - John Doe")
    bottom.geometry("500x500")

    def push():
        web = website.get()
        mail = email.get()
        usrnm = username.get()
        paswd = password.get()
        global uk
        enc_pass = Encrypt(paswd, uk).decode()
        descrip = str(clicked.get())

        acc = sqlite3.connect(f"{u}.db")
        a = acc.cursor()
        a.execute("INSERT INTO passwords VALUES('"+web+"','"+usrnm+"','"+mail+"','"+enc_pass+"','"+descrip+"')")
        messagebox.showinfo("Information", "Successfully Inserted!")

        acc.commit()
        acc.close()

    lbltitle = Label(bottom, bd=20, text="Enter Details", bg="white", font=("times new roman", 22, "bold"))
    lbltitle.pack(side=TOP, fill=X)

    Entryframe = Frame(bottom, bd=12, relief=RIDGE)
    Entryframe.place(x=0, y=90, width
