def fun(var1=100, var2=200):
    var1 += 10
    var2 = var2 - 10
    return var1 + var2
print(fun(50),fun())

S='WELCOME'
def change(T):
    T='HELLO'
    print(T,end='@')
change(S)
print(S)

def add(num1,num2):
    sum = num1 + num2
    return sum
sum = add(20,30)
print(sum)
