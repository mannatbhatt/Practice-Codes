import mysql.connector
import tkinter as tk
from tkinter import messagebox
import subprocess

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

cs.execute("use shoppingportal")

#ADDING PRODUCT FUNCTION
def enterval():
    try:
        x = entry_category.get()
        cs.execute("SELECT typeid FROM pcategory WHERE type=%s", (x,))
        tid = cs.fetchone()

        if tid:
            category = x
            gender = entry_gender.get()
            size = entry_size.get()
            price = entry_price.get()

            # inserting into the product table
            query = "INSERT INTO product(typeid, category, gender, size, price) VALUES (%s, %s, %s, %s, %s)"
            val = (tid[0], category, gender, size, price)

            cs.execute(query, val)
            mydb.commit()
            cs.execute("UPDATE product SET itemcode = CONCAT(typeid,autoinc)")

            cs.execute(
                "SELECT itemcode FROM product WHERE autoinc = (SELECT MAX(autoinc) FROM product)"
            )
            pid = cs.fetchone()

            # inserting into the stock table
            query2 = "INSERT INTO stock(itemcode, stock) VALUES (%s, %s)"
            val2 = (pid[0], 0)

            cs.execute(query2, val2)
            mydb.commit()
            messagebox.showinfo("Product Added", "Product Added successfully!")
            root.destroy()
            subprocess.run(["python", "Admin/AMain.py"])

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#BACK
def back():
    root.destroy()
    subprocess.run(["python", "Admin/AMain.py"])

#GUI

#VARIABLES
wsize=40
wfontsize=15
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wfont="comic sans ms"
wbox="#fce3f6"

#OPENING WINDOW
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Add Product Details")

#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")


#CATEGORY
tk.Label(frame, text="ENTER CATEGORY",font=(wfont, wfontsize), bg=wcolour).pack()
entry_category = tk.StringVar()
entry_category.set("Choose")  # Default value
cat_menu = tk.OptionMenu(frame,entry_category, "SHIRT","TROUSER","SHOES","ACCESSORY","HOUSEHOLD")
cat_menu.pack(pady=10)

#GENDER
tk.Label(frame, text="ENTER GENDER",font=(wfont, wfontsize), bg=wcolour).pack()
entry_gender = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_gender.pack(pady=10)

#SIZE
tk.Label(frame, text="ENTER SIZE",font=(wfont, wfontsize), bg=wcolour).pack()
entry_size = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_size.pack(pady=10)

#PRICE
tk.Label(frame, text="ENTER PRICE",font=(wfont, wfontsize), bg=wcolour).pack()
entry_price = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_price.pack(pady=10)

#ADD PRODUCT
enter_value_button = tk.Button(frame, text="ADD PRODUCT",font=(wfont, 20),bg="#e3f5fc", command=enterval)
enter_value_button.pack(pady=70)

#back button
navback = tk.Button(frame, text="BACK",font=(wfont, 20),bg="#e3f5fc", command=back)
navback.pack(pady=20)
navback.config(width=5, height=1)

root.mainloop()
