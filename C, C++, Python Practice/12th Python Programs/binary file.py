import pickle
with open("newfile.dat","rb+") as f:
    while True:
        try:
            fp=f.tell()
            read=pickle.load(f)
            if read[0]=="Arya":
                read[2]=="55000"
                f.seek(fp,0)
                pickle.dump(read,f)
        except EOFError:
                break
print(read)
