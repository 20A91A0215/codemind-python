n=int(input())
rev=1
sum=0
while n>0:#234 23
    r=n%10#r=4 3
    rev=rev*r
    sum=sum+r
    n=n//10
res=rev-sum
print(res)
    
    