n=input()
k=[]
s=0
for i in n:
    k.append(int(i))
for i in range(len(n)):
    s=s+k[i]**(i+1)
print(int(n)==s)