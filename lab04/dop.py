n=int(input("Введите число: "))
dev=2
f=0

while (dev*dev<=n):
    if (n%dev==0):
        f=1
    dev+=1
if (f==1):
    print("Простое")
else:
    print("Не простое")
