import math
i=0
j=0
k=0
while i<500:
    while j<i:
        while k<j:
            if math.pow(i,2)==math.pow(j,2)+math.pow(k,2):
                print i+j+k,i,j,k
            k+=1
        j+=1
    i+=1
