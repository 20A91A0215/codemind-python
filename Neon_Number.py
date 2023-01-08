n=int(input())
m=n*n
m=str(m)
d=0
for i in m:
    d=d+int(i)
if(d==n):
    print("Neon Number")
else:
    print("Not Neon Number")