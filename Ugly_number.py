n=int(input())
m=n
c=1
#print
if(n>0):
    for i in range(n):
        if n%2==0:
            c=c*2
            n=n//2
           # print(c,n)
if n>0:
    for i in range(n):
        if n%3==0:
            c=c*3
            n=n//3
           # print(c,n)
if n>0:
    for i in range(n):
        if n%5==0:
            c=c*5
            n=5//2
           # print(c,n)
if c==m:
    print("Ugly Number")
else:
    print("Not Ugly Number")