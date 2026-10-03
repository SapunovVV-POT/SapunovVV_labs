a=int(input("Введите число:"))
b=int(input("Введите число:"))
i=a
if (a>b):
    while (i+1>b):
        print(i)
        i=i-1
elif (a<b):
    while (i-1<b):
        print(i)
        i=i+1
else:
    print(i)
