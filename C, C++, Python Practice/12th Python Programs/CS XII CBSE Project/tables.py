import mysql.connector
x=input("Enter your password:")
mydb = mysql.connector.connect(host="localhost",user="root",password=str(x))
cs=mydb.cursor()

def db():
    cs.execute("create database shoppingportal")
    cs.execute("use shoppingportal")

def tables():
    query1=("Create table product (typeid int references pcategory(typeid) ,itemcode integer(3) unique,category varchar(30),gender varchar(1) ,size varchar(3),price integer(4) not null,autoinc int(40) auto_increment primary key);")
    query2=("Create table orderdetails (orderid integer(3) auto_increment primary key unique not null,customerid integer(3) references customerdetails(CID),itemcode integer(3) references product(itemcode),quantity integer(2) not null,dateofpurchase date,shippingaddress varchar(50) not null);")
    query3=("Create table stock (itemcode integer(3) references product(itemcode),stock integer(5));")
    query4=("CREATE TABLE pickupportal (material VARCHAR(30),weight DECIMAL(10,2),materialcondition VARCHAR(10),cid INT(3) REFERENCES customer(cid),streetaddress VARCHAR(50),postalcode VARCHAR(6),town VARCHAR(20));")
    query5=("Create table deliverysystem(orderid int references orderdetails(orderid),cid int references customer(cid),postalcode int(6), town varchar(20));")
    query6=("CREATE TABLE customer(cid integer(3) primary key auto_increment,firstname varchar(20), lastname varchar(20), phone integer(10) unique, pass VARCHAR(50) NOT NULL,userid varchar(30) unique);")
    query7=("Create table pcategory(typeid integer(2) not null primary key,type varchar(30))")

    query21=("Insert into pcategory values(35,'shirt'),(36,'trouser'),(37,'shoes'),(38,'accessory'),(39,'household');")
    cs.execute(query1)
    print("Product table created successfully")
    cs.execute(query2)
    print("Order Details table created successfully")
    cs.execute(query3)
    print("Stock table created successfully")
    cs.execute(query4)
    print("Pickup Details table created successfully")

    cs.execute(query5)
    print("Delivery Details table created successfully")

    cs.execute(query6)
    print("Customer Details table created successfully")

    cs.execute(query7)
    print("Product category table created successfully")

    cs.execute(query21)
    print("Category added to table successfully")


x=int(input('''
Do you want to create the tables?
    1:Yes
    2:No
'''))
if x==1:
    db()
    tables()
elif x==2:
    cs.execute("use shoppingportal")
    print("Using shoppingportal")

