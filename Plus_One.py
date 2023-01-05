n=int(input())
li=list(map(int,input().split()))
a=" "
for i in li:
    a+=str(i)
b=int(a)+1
c=str(b)
for i in c:
    print(i,end=" ")