import mysql.connector
import tkinter as tk
import subprocess

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

cs.execute("use shoppingportal")

#LOGIN
def logincli():
    root.destroy()  # close this window and open below mentioned python program using subprocesss
    subprocess.run(["python", "Login.py"])

#REGISTERATION
def regiscli():
    root.destroy()
    subprocess.run(["python", "Register.py"])

#GUI

#VARIABLES
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wfont='comic sans ms'

#OPENING WINDOW
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Login/Register")




#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")


#LOGIN
login_button = tk.Button(frame, text="Login",font=(wfont, 20),bg="#e3f5fc", command=logincli)
login_button.pack(pady=10)
login_button.config(width=20, height=4)


#REGISTERATION
register_button = tk.Button(frame, text="Register",font=(wfont, 20),bg="#e3f5fc", command=regiscli)
register_button.pack(pady=10)
register_button.config(width=20, height=4)

root.mainloop()
