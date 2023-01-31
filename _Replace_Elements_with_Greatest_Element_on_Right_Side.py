n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)-1):
    h=i+1
    ll=l[h:]
    u=max(ll)
    k.append(u)
k.append(-1)
print(*k)