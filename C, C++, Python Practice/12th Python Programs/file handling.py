f=open("empty.txt","w")
data = "I am Mannat"

f.write(data)
f.close()

f=open("empty.txt","a")
f.write(" from 12 Science")
f.close()

f=open("empty.txt","r")
a=f.read()
print(a)

with open("empty.txt","r") as f:
    b=f.read(3)
    print(b)

