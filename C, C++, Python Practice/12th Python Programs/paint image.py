import pickle
with open("paint.dat","rb") as f:
    str = " "
    str1 = pickle.load(f)
    str = str1.split("O")
    c = pickle.load(str)
    print(c)
