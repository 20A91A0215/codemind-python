n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    ll=list(map(int,input().split()))
    l.extend(ll)
    l.sort()
    print(*l)