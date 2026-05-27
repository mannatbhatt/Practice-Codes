import mysql.connector
import tkinter as tk
import subprocess
mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

cs.execute("use shoppingportal")


def add_stock():
    root.destroy()
    subprocess.run(["python", "Admin/Stock.py"])


def enter_val():
    root.destroy()
    subprocess.run(["python", "Admin/Product.py"])


def del_product():
    root.destroy()
    subprocess.run(["python", "Admin/Delete.py"])


def logout():
    root.destroy()
    subprocess.run(["python", "Main.py"])


#variables
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wfont="comic sans ms"

#OPENING WINDOW
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("ADMIN ACCESS")

#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")



#BOOK BUTTON
enterval_button = tk.Button(frame, text="ADD PRODUCT",font=(wfont, 20),bg="#e3f5fc", command=enter_val)
enterval_button.pack(pady=20)
enterval_button.config(width=20, height=2)

#DELETE PRODUCT
delval_button = tk.Button(frame, text="DELETE PRODUCT",font=(wfont, 20),bg="#e3f5fc", command=del_product)
delval_button.pack(pady=20)
delval_button.config(width=20, height=2)

#UPDATE STOCK
delval_button = tk.Button(frame, text="UPDATE STOCK",font=(wfont, 20),bg="#e3f5fc", command=add_stock)
delval_button.pack(pady=20)
delval_button.config(width=20, height=2)

#LOGOUT
delval_button = tk.Button(frame, text="LOGOUT",font=(wfont, 20),bg="#e3f5fc", command=logout)
delval_button.pack(pady=20)
delval_button.config(width=20, height=2)

root.mainloop()
