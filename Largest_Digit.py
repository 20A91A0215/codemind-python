s=int(input())
rev=0
while s>0:
    t=s%10
    if t>rev:
      rev=t
    s=s//10
print(rev)