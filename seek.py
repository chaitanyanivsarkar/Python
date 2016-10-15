f=file("E:\\harsh.txt","a+")
while True:
    position=f.tell()
    rec=f.readline()
    if rec.find("akash")!=-1:
        rec=rec.replace("akash","harsh")
        f.seek(position)
        f.write(rec)
    break
f.close
    
