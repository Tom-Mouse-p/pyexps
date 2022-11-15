import sqlite3
import tkinter as tk
db = sqlite3.connect("users.db")
db.execute('CREATE TABLE IF NOT EXISTS USER_DB(USERNAME text, PASSWORD text)')
db.commit()

db.execute("SELECT * FROM USER_DB")

def register():
    uname = username.get()
    pword = password.get()

    if uname == "" or pword == "":
        print("Empty Field!")
    else:
        db.execute('INSERT INTO USER_DB (USERNAME, PASSWORD) VALUES(?,?)', (uname, pword))
        db.commit()
        print("Inserted")
    db.execute("SELECT * FROM USER_DB")
    db.commit()


def login():
    unname = username.get()
    pword = password.get()


root = tk.Tk()
root.title("Pranav | Login")
root.geometry('500x500-0-0')
title = tk.Label(root, text="Login/Signup Page")
username = tk.Entry(root)
password = tk.Entry(root)
reg_btn = tk.Button(root, text="Register", command="register")
login_btn = tk.Button(root, text="Login", command="login")

title.pack()
username.pack()
password.pack()
reg_btn.pack()
login_btn.pack()
root.mainloop()
