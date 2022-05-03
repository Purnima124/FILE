# f=open("people1-exerise.txt","r")
f=open("people1-exerise.txt","w")
for i in f:
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
    elif "shimla" in i:
        f=open("shimla.txt","a")
        f.write(i)
    else:
        f=open("other.txt","a")
        f.write(i)
f.close()