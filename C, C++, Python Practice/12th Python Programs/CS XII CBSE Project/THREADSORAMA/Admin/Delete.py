import mysql.connector
import tkinter as tk
import subprocess
from tkinter import messagebox

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

cs.execute("use shoppingportal")

#DELETE PRODUCT FUNCTION
def delproduct():
    try:
        product_id = entry_product_id.get()
        query = "SELECT * FROM product WHERE itemcode = %s"
        val = (product_id,)
        cs.execute(query, val)
        result = cs.fetchone()

        if not result:
            messagebox.showinfo("Error", "Product does not exist")
        else:
            query = "DELETE FROM product WHERE itemcode = %s"
            cs.execute(query, (product_id,))
            query = "DELETE FROM stock WHERE itemcode = %s"
            cs.execute(query, (product_id,))
            mydb.commit()
            messagebox.showinfo("Product Deleted", "Product deleted successful!")
            root.destroy()
            subprocess.run(["python", "Admin/AMain.py"])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#BACK NAVIGATION FUNCTION
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
root.title("Delete Product")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")

#PRODUCT ID
tk.Label(frame, text="ENTER PRODUCT ID",width=wsize, font=(wfont, wfontsize), bg=wcolour).pack()
entry_product_id = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_product_id.pack(pady=20)

#DELETE PRODUCT
delete_product_button = tk.Button(frame, text="DELETE PRODUCT",width=20,font=(wfont,wfontsize),bg=wbox, command=delproduct)
delete_product_button.pack(pady=50)

#BACK BUTTON
navback = tk.Button(frame, text="BACK",font=(wfont, 20),bg="#e3f5fc", command=back)
navback.pack(pady=20)
navback.config(width=5, height=1)

root.mainloop()
