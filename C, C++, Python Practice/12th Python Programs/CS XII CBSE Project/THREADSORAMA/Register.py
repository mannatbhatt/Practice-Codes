import mysql.connector
import tkinter as tk
from tkinter import messagebox
import subprocess

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007
                               ")
cs = mydb.cursor()

cs.execute("use shoppingportal")

#PASSWORD CHECK FUNCTION
def passcheck(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;':,.<>/?":
            has_special = True
        elif char.isspace():
            has_space = True

    return (
        len(password) >= 8
        and has_upper
        and has_lower
        and has_digit
        and has_special
        and not has_space
    )

#REGISTERATION FUNCTION
def regiscli():
    try:
        user = entry_user.get()
        fname = entry_fname.get()
        lname = entry_lname.get()
        phone = entry_phone.get()
        password = entry_password.get()

        while True:
            if passcheck(password):
                break
            else:
                messagebox.showinfo(
                    "Weak Password",
                    """
    Password is weak. Please consider the following guidelines:
        - Use a combination of uppercase and lowercase letters
        - Include at least one digit
        - Add at least one special character (!@#$%^&*()_+-=[]{}|;':\",.<>/?
        - Make the password at least 8 characters long
        - Do not use spaces in the password""",
                )
                return

        query = "SELECT * FROM customer WHERE userid = %s"
        val = (user,)
        cs.execute(query, val)
        result = cs.fetchone()
        if result:
            messagebox.showinfo(
                "Username Exists", "Username already exists. Please try a different one."
            )
            return

        query = "INSERT INTO customer (firstname, lastname, phone, pass, userid) VALUES (%s, %s, %s, %s, %s)"
        val = (fname, lname, phone, password, user)
        cs.execute(query, val)
        mydb.commit()

        messagebox.showinfo("Registration Successful", "User registered successfully!")
        root.destroy()
        subprocess.run(["python", "Main.py"])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#GUI

#VARIABLES
wsize=40
wfontsize=20
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wbox="#fce3f6"
wfont='comic sans ms'

#OPENING WINDOW
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")

#USERNAME
tk.Label(frame, text="USERNAME", font=(wfont, wfontsize), bg=wcolour).pack()
entry_user = tk.Entry(frame,width=wsize,font=(wfont, wfontsize),bg=wbox)
entry_user.pack(pady=20)

#FIRST NAME
tk.Label(frame, text="FIRST NAME", font=(wfont, wfontsize), bg=wcolour).pack()
entry_fname = tk.Entry(frame,width=wsize,font=(wfont, wfontsize,),bg=wbox)
entry_fname.pack(pady=20)

#LAST NAME
tk.Label(frame, text="LAST NAME", font=(wfont, wfontsize), bg=wcolour).pack()
entry_lname = tk.Entry(frame,width=wsize,font=(wfont, wfontsize),bg=wbox)
entry_lname.pack(pady=20)

#PHONE NO
tk.Label(frame, text="PHONE", font=(wfont, wfontsize), bg=wcolour).pack()
entry_phone = tk.Entry(frame,width=wsize,font=(wfont, wfontsize),bg=wbox)
entry_phone.pack(pady=20)

#PASSWORD
tk.Label(frame, text="PASSWORD", font=(wfont, wfontsize), bg=wcolour).pack()
entry_password = tk.Entry(frame, show="*",width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_password.pack(pady=20)

#REGISTER BUTTON
register_button = tk.Button(frame, text="REGISTER",font=(wfont, 20),bg="#e3f5fc", command=regiscli)
register_button.pack(pady=80)

root.mainloop()
