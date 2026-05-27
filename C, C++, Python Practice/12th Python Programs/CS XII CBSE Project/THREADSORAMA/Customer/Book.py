import subprocess
import tkinter as tk
from tkinter import messagebox
import os
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="mannatbhatt@2007")
cs = mydb.cursor()

permanentcid = os.environ.get("permanentcid")
cs.execute("use shoppingportal")

#BOOK FUNCTION
def book():
    try:

        global permanentcid
        mat = entry_material.get()
        w = entry_weight.get()
        mcondition = condition_var.get()
        sadd = entry_street_address.get()
        pcode = entry_postal_code.get()
        town = entry_town.get()

        query = "INSERT INTO pickupportal VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (mat, w, mcondition, permanentcid, sadd, pcode, town)

        cs.execute(query, val)
        mydb.commit()

        messagebox.showinfo("Booking Successful", "Booking successful!")
        root.destroy()
        subprocess.run(["python", "Customer/Cmain.py"])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#BACK FUNCTION
def back():
    root.destroy()
    subprocess.run(["python", "Customer/CMain.py"])

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
root.title("Booking")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("BOOK PICKUP")

#CANVAS AND FRAME
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(root,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")

#MATERIAL
tk.Label(frame, text="Choose Material:",font=(wfont, wfontsize), bg=wcolour).pack()
entry_material = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_material.pack(pady=10)

#WEIGHT
tk.Label(frame, text="Enter Weight:",font=(wfont, wfontsize), bg=wcolour).pack()
entry_weight = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_weight.pack(pady=10)

#CONDITION
tk.Label(frame, text="Enter Condition:",font=(wfont, wfontsize), bg=wcolour).pack()
condition_var = tk.StringVar()
condition_var.set("Choose")  # Default value
condition_menu = tk.OptionMenu(frame,condition_var, "Worn out", "Average", "Brand New")
condition_menu.pack(pady=10)

#STREET ADDRESS
tk.Label(frame, text="Enter Street Address:",font=(wfont, wfontsize), bg=wcolour).pack()
entry_street_address = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_street_address.pack(pady=10)

#POSTAL CODE
tk.Label(frame, text="Enter Postal Code:",font=(wfont, wfontsize), bg=wcolour).pack()
entry_postal_code = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_postal_code.pack(pady=10)

#TOWN
tk.Label(frame, text="Enter Town:",font=(wfont, wfontsize), bg=wcolour).pack()
entry_town = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_town.pack(pady=10)

#BOOK
book_button = tk.Button(frame, text="Book Pickup",width=10,font=(wfont,wfontsize),bg="#e3f5fc", command=book)
book_button.pack(pady=10)

#BACK
navback = tk.Button(frame, text="BACK",font=(wfont, 20),bg="#e3f5fc", command=back)
navback.pack(pady=20)
navback.config(width=5, height=1)


root.mainloop()
