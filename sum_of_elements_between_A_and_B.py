n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
z=[]
for i in l:
    if(i>=a and i<=b):
        z.append(i)
print(sum(z))