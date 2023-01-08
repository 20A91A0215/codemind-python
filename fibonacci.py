n=int(input())
k=[0,1]
s=1
for i in range(2,n):
    x=k[i-1]+k[i-2]
    k.append(x)
print(*k)