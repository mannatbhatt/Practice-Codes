import mysql.connector
from datetime import datetime
import tkinter as tk
import subprocess

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()
date = datetime.now()

cs.execute("use shoppingportal")

#BOOK A PICKUP
def bookcli():
    root.destroy()
    subprocess.run(["python", "Customer/Book.py"])

#ORDER
def place_order():
    root.destroy()
    subprocess.run(["python", "Customer/Order.py"])

#LOGOUT
def logout():
    root.destroy()
    subprocess.run(["python", "Main.py"])

#GUI

#VARIABLES
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wfont="comic sans ms"

#OPENING WINDOW
root = tk.Tk()
root.title("THREADSORAMA")

#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")

#BOOK PICKUP
book_button = tk.Button(frame, text="BOOK A PICKUP",font=(wfont, 20),bg="#e3f5fc", command=bookcli)
book_button.pack(pady=10)
book_button.config(width=20, height=4)

#PLACE ORDER
order_button = tk.Button(frame, text="ORDER",font=(wfont, 20),bg="#e3f5fc", command=place_order)
order_button.pack(pady=20)
order_button.config(width=20, height=4)

#LOGOUT
delval_button = tk.Button(frame, text="LOGOUT",font=(wfont, 20),bg="#e3f5fc", command=logout)
delval_button.pack(pady=20)
delval_button.config(width=20, height=4)


root.mainloop()
