n=input()
k=[]
for i in n:
    k.append(int(i))
s=list(set(k))
if(len(s)==len(k)):
    print("Unique Number")
else:
    print("Not Unique Number")