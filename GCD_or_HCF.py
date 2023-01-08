n,m=map(int,input().split())
k=[]
kk=[]
for i in range(1,n+1):
    if n%i==0:
        k.append(i)
for i in range(1,m+1):
    if m%i==0:
        kk.append(i)
v=[]
for i in k:
    if i in kk:
        v.append(i)
print(max(v))