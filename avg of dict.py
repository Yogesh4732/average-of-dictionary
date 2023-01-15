n=int(input())
d=dict()
sum=0
for i in range(n):
    key=input("Key: ")
    val=int(input("value: "))
    d[key]=val
    sum+=val
print(sum//n)
