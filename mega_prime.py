n=int(input())
c=0
x=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
n=str(n)
for i in n:
    if(i=="2" or i=="3" or i=="5" or i=="7"):
        x=x+1
if(c==2 and x==len(n)):
    print("Mega Prime")
else:
    print("Not Mega Prime")