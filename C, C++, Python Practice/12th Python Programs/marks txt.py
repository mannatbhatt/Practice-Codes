count=int(input("Enter the number of students "))
file = open("Marks.txt","w")
for i in range(count):
    print("Enter the details for student ",(i+1),"below: ")
    roll=int(input("Enter the roll no. "))
    name=input("Enter the name ")
    marks=float(input("Enter the marks "))
    rec=str(roll)+" "+name+" "+str(marks) + "\n"
    file.write(rec)
file.close()
f1 = open("Marks.txt","a")
for i in range(1):
    print("Enter the details for student ",(i+1),"below: ")
    roll=int(input("Enter the roll no. "))
    name=input("Enter the name ")
    marks=float(input("Enter the marks "))
    rec=str(roll)+" "+name+" "+str(marks) + "\n"
    f1.write(rec)
f1.close()
file=open("Marks.txt","r")
while str:
    str=file.readline()
#use split() to print line word by word, ek ek line leke words ko split kr
    for word in str.split():
        print(word,end=",")
    print()
file.close()
