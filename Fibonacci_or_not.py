n=int(input())
k=[0,1]
for i in range(2,100):
    k.append(k[i-1]+k[i-2])

if n in k:
    print("True")
else:
    print("False")