f=open("empty.txt","r")
str1=f.read()

str2=f.readlines()

str3=f.readline()
print(str1)
print(str2)
print(str3)

f.close()

with open('empty.txt', 'r') as file:
        data = file.read(3)
        print("File contents:")
        print(data)
