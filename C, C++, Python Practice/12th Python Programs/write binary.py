import pickle
with open("newfile.dat","wb") as f:
    L1=["Arya","21","20000"]
    L2=["Priya","33","33000"]
    L3=["Daya","22", "43000"]
    pickle.dump(L1,f)
    pickle.dump(L2,f)
    pickle.dump(L3,f)
