n=int(input())
prt=1
sum=0
while n>0:
    r=n%10
    prt=prt*r
    sum=sum+r
    n=n//10
if prt==sum:
    print("Spy Number")
else:
    print("Not Spy Number")