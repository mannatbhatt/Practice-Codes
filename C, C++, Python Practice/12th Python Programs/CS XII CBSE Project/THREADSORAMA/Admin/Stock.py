import mysql.connector
import tkinter as tk
from tkinter import messagebox
import subprocess

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

cs.execute("use shoppingportal")

#ADDING STOCK FUNCTION
def addstock():
    try:
        item_code = entry_item_code.get()
        stock = entry_stock.get()

        # check if the item code exists in the stock table
        cs.execute("SELECT * FROM stock WHERE itemcode = %s", (item_code,))
        existing_stock = cs.fetchone()

        if existing_stock:
            # item code exists, updates the stock
            query = "UPDATE stock SET stock = stock + %s WHERE itemcode = %s"
            val = (stock, item_code)
            cs.execute(query, val)
        else:
            # item code does not exist, insert a new record
            query = "INSERT INTO stock (itemcode, stock) VALUES (%s, %s)"
            val = (item_code, stock)
            cs.execute(query, val)

        mydb.commit()
        messagebox.showinfo("Stock Added", "Stock updated successfully!")
        root.destroy()
        subprocess.run(["python", "Admin/Amain.py"])

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#BACK NAVIGATION FUNCTION
def back():
    root.destroy()
    subprocess.run(["python", "Admin/AMain.py"])

#GUI

#OPENING WINDOW
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Add Stock")

#VARIABLES
wsize=40
wfontsize=15
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wfont="comic sans ms"
wbox="#fce3f6"

#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")


#ITEMCODE
tk.Label(frame, text="ENTER ITEMCODE",font=(wfont, wfontsize), bg=wcolour).pack()
entry_item_code = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_item_code.pack(pady=20)

#STOCK
tk.Label(frame, text="ENTER STOCK",font=(wfont, wfontsize), bg=wcolour).pack()
entry_stock = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_stock.pack(pady=20)

#ADD STOCK
add_stock_button = tk.Button(frame, text="Add Stock",font=(wfont, 20),bg="#e3f5fc", command=addstock)
add_stock_button.pack(pady=50)

#BACK
navback = tk.Button(frame, text="BACK",font=(wfont, 20),bg="#e3f5fc", command=back)
navback.pack(pady=20)
navback.config(width=5, height=1)

root.mainloop()
