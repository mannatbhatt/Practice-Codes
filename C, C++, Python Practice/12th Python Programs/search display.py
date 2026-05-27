import csv
def create():
    with open("data.csv","w",newline="") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(["User ID","Password"])
        while True:
            u_id=input("Enter the User ID: ")
            pwd=input("Enter the Password: ")
            rec=[u_id,pwd]
            fobj.writerow(rec)

            ch=int(input("Enter choice, to continue - 1, to break - 2"))
            if ch==2:
                break
def display():
    with open("data.csv","r") as obj:
        read=csv.reader(obj)
        for i in read:
            print(i)
def search():
    while True:
        with open("data.csv", "r") as obj:
            search = csv.reader(obj)
            u_id = input("Enter the user ID (or type 'exit' to quit): ")
            if u_id.lower() == 'exit':
                break
            found = False
            for i in search:
                if i[0] == u_id:
                    print("Password for", u_id, "is:", i[1])
                    found = True
                    break
            if found==False: #or you can write (if not found:)
                print("User ID not found.")
ch=int(input("Enter the choice : 1 - Create, 2 - Display, 3 - Search"))
if ch==1:
    create()
if ch==2:
    display()
if ch==3:
    search()
