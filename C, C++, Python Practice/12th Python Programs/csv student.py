import csv
with open("stu.csv","w") as obj:
    fobj = csv.writer(obj)
    fobj.writerow(["Roll no.", "Name", "Marks"])

    while True:
        rollnum = int(input("Enter the roll number "))
        name =input("Enter the name ")
        marks = int(input("Enter marks "))
        rec = [rollnum, name, marks]
        fobj.writerow([rollnum, name, marks])

        ch = int(input("Enter the value - 1 to continue, 2 - to stop "))
        if ch == 2:
           break
