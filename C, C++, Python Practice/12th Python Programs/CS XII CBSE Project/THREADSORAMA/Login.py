import mysql.connector
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

#VARIABLE(TO BE USED LATER)
permanentcid = 0
adminid=50

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

cs.execute("use shoppingportal")

#LOGIN FUNCTION
def login():
    try:

        user = entry_user.get()

        query_user = "SELECT * FROM customer WHERE userid = %s"
        val_user = (user,)
        cs.execute(query_user, val_user)
        result_user = cs.fetchone()

        if not result_user:
            messagebox.showinfo(
                "Invalid Username", "Username does not exist. Please try again."
            )
            return

        while True:
            password = entry_password.get()
            sql = "SELECT * FROM customer WHERE pass = %s AND userid = %s"
            val = (password, user)
            cs.execute(sql, val)
            result = cs.fetchone()

            if result:
                global permanentcid
                global adminid
                query = "select cid from customer where userid=%s"
                cs.execute(query, (user,))
                x = cs.fetchone()
                permanentcid = x[0]
                messagebox.showinfo("Login Successful", "Login successful!")
                os.environ["permanentcid"] = str(permanentcid)

                if permanentcid == adminid:
                    root.destroy()
                    subprocess.run(["python", "Admin/AMain.py"])
                else:
                    root.destroy()
                    subprocess.run(["python", "Customer/CMain.py"])
                break
            else:
                messagebox.showinfo("Invalid Password", "Invalid password. Please try again.")
                return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


#GUI

#VARIABLES

wsize = 40
wfontsize = 20
window_width = 1550
window_height = 1000
wcolour = "#f5bae5"
wbox = "#fce3f6"
wfont = 'comic sans ms'

#OPENING WINDOW
root = tk.Tk()
root.title("Login Page")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame = tk.Frame(root , bg=wcolour)
frame.pack(expand=True , fill = "both")
frame.place(relx=0.5 , rely=0.5 , anchor="center")


#USERNAME
tk.Label(frame, text="USERNAME" , font = (wfont , wfontsize) , bg= wcolour).pack()
entry_user = tk.Entry(frame , width = wsize , font = (wfont,wfontsize) , bg=wbox)
entry_user.pack(pady=20)

#PASSWORD
tk.Label(frame, text="PASSWORD" , font=(wfont, wfontsize), bg=wcolour).pack()
entry_password = tk.Entry(frame , show="*" , width=wsize,font=(wfont , wfontsize) , bg=wbox)
entry_password.pack(pady=20)

#LOGIN BUTTON
login_button = tk.Button(frame , text="LOGIN" , width=10 , font=(wfont , wfontsize) , bg="#e3f5fc" , command=login)
login_button.pack(pady=50)

root.mainloop()
