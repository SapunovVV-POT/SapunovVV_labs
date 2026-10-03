a=int(input("Введите число: "))
b=int(input("Введите число еще раз: "))
c=int(input("Введите число последний раз: "))

if (a<b and a<c):
    min_number=a
elif (b<a and b<c):
    min_number=b
else:
    min_number=c
    
print("Минимальное число: ", min_number)
