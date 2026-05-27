import mysql.connector
from datetime import date
import tkinter as tk
from tkinter import messagebox, Entry
import os
import subprocess

permanentcid = os.environ.get("permanentcid")

mydb = mysql.connector.connect(
    host="localhost", user="root", password="mannatbhatt@2007", database="shoppingportal"
)
cs = mydb.cursor()

#VARIABLES
wsize=40
wfontsize=15
window_width = 1550
window_height = 1000
wcolour= "#f5bae5"
wfont="comic sans ms"
wbox="#fce3f6"

#OPENING WINDOW
my_w = tk.Tk()
my_w.geometry("{0}x{1}+0+0".format(my_w.winfo_screenwidth(), my_w.winfo_screenheight()))
my_w.title("Shopping Portal")

#CANVAS AND FRAME
canvas = tk.Canvas(my_w, width=window_width, height=window_height, bg=wcolour)  # Set canvas background to pink
canvas.pack()

frame=tk.Frame(my_w,bg=wcolour)
frame.pack(expand=True,fill="both")
frame.place(relx=0.5,rely=0.5,anchor="center")

#STOCK DISPLAY
cs.execute("SELECT p.itemcode,p.category,p.gender,p.size,p.price,s.stock FROM product p JOIN stock s ON p.itemcode = s.itemcode;")
stock_column_names = [desc[0] for desc in cs.description]




#CREATING LABLES(PRODUCT ID AND STOCK
for j in range(len(stock_column_names)):
    label = tk.Label(frame, text=stock_column_names[j].upper(), font=(wfont, 20),bg=wcolour)
    label.grid(row=0, column=j)

i = 1
for stock_data in cs:
    for j in range(len(stock_data)):
        e = Entry(frame, width=10, fg="green", font=(wfont, 12))
        e.grid(row=i, column=j)
        e.insert(tk.END, stock_data[j])
    i += 1

#ORDER FUNCTION
def placingorder():
    try:
        # working
        global permanentcid
        cid = str(permanentcid)
        today = date.today()
        ic = str(entry_product_id.get())
        qt = str(entry_quantity.get())
        dop = str(today.strftime("20%y-%m-%d"))
        sadd = str(entry_shipping_address.get())
        pcode = str(entry_postal_code.get())
        town = str(entry_town.get())

        # working
        query = "INSERT INTO orderdetails (customerid, itemcode, quantity, dateofpurchase, shippingaddress) VALUES (%s, %s, %s, %s, %s)"
        val = (cid, ic, qt, dop, sadd)

        cs.execute(query, val)

        mydb.commit()

        # not working
        cs.execute("SELECT max(orderid) from orderdetails")
        x = cs.fetchone()
        oid = x[0]

        # this is working
        query = "INSERT INTO deliverysystem VALUES (%s, %s, %s, %s)"
        val = (str(oid), str(cid), str(pcode), str(town))

        cs.execute(query, val)
        mydb.commit()

        query2 = "UPDATE stock SET stock = stock - %s WHERE itemcode = %s"
        val2 = (str(qt), str(ic))

        cs.execute(query2, val2)
        mydb.commit()

        messagebox.showinfo("Order Placed", "Order placed successfully!")
        my_w.destroy()
        subprocess.run(["python", "Customer/Cmain.py"])

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#BACK NAVIGATION
def back():
    my_w.destroy()
    subprocess.run(["python", "Customer/CMain.py"])


#PRODUCT ID
tk.Label(frame, text="Enter Product ID:",font=(wfont, wfontsize), bg=wcolour).grid(row=i, column=0)
entry_product_id = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_product_id.grid(row=i, column=1,pady=5)
i += 1

#QUANTITY
tk.Label(frame, text="Enter Quantity:",font=(wfont, wfontsize), bg=wcolour).grid(row=i, column=0)
entry_quantity = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_quantity.grid(row=i, column=1,pady=5)
i += 1

#SHIPPING ADDRESS
tk.Label(frame, text="Enter Shipping Address:",font=(wfont, wfontsize), bg=wcolour).grid(row=i, column=0)
entry_shipping_address = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_shipping_address.grid(row=i, column=1,pady=5)
i += 1

#POSTAL CODE
tk.Label(frame, text="Enter Postal Code:",font=(wfont, wfontsize), bg=wcolour).grid(row=i, column=0)
entry_postal_code = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_postal_code.grid(row=i, column=1,pady=5)
i += 1

#TOWN
tk.Label(frame, text="Enter Town:",font=(wfont, wfontsize), bg=wcolour).grid(row=i, column=0)
entry_town = tk.Entry(frame,width=wsize,font=(wfont,wfontsize),bg=wbox)
entry_town.grid(row=i, column=1,pady=5)
i += 1

#PLACE ORDER BUTTON
place_order_button = tk.Button(frame, text="Place Order",font=(wfont, 20),bg="#e3f5fc", command=placingorder)
place_order_button.grid(row=i, column=0, columnspan=2, pady=20)
i+=1

#BACK BUTTON
navback = tk.Button(frame, text="BACK",font=(wfont, 20),bg="#e3f5fc", command=back)
navback.grid(row=i, column=0, columnspan=2, pady=5)


my_w.mainloop()
