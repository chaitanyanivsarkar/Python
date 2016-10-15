import os
f1=open("E:\\write.txt","a+")
f2=open("E:\\temp.txt","w+")
count=0
rec=" "
while rec :
    rec=f1.readline()
    count=count+1
    if count==3:
        pass
    else:
        f2.write(rec)
    f1.close()
    f2.close()
    os.remove("E:\\write.txt")
    os.rename("E:\\temp.txt","E:\\write.txt")
