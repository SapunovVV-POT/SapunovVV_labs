n_try=0
a=int(input("Введите число: "))
while (a<=0):
    a=int(input("Введите число: "))
    n_try=n_try+1
print("Количество неудачных попыток: ", n_try)
s=a*a
print("Квадрат введенного числа: ",s)
