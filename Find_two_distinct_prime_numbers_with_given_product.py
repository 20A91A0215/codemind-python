n=int(input())
k=[]
for i in range(1,n+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            k.append(i)
z=[]
for i in k:
    for j in k:
        if(i*j==n):
            z.append(i)
            z.append(j)
if(z==[]):
    print(-1)
else:
    print(z[0],z[1])