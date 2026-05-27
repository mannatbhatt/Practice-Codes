n1= int(input("Enter the number: "))
c=input("Enter the operator ")
n2= int(input("Enter the number: "))
def calc(a,b):
    if c=="+":
        print("SUM ",a+b)
    elif c=="-":
        print("DIFFERENCE ",a-b)
    elif c=="x" or c=="X":
        print("PRODUCT ",a*b)
    elif c=="/":
        print("QUOTIENT ",a/b)
    elif c=="%":
        print("REMAINDER ",a%b)
    else:
        print("Invalid")
calc(n1,n2)
