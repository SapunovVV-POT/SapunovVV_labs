num_1=int(input("Введите число:"))
num_2=int(input("Введите второе число: "))
sign=input("Введите знак (+,-,*,/): ")

if sign == '+':
    print(f'{num_1 + num_2:.2f}')
elif sign == '-':
    print(f'{num1 - num2:.2f}')
elif sign == '*':
    print(f'{num1 * num2:.2f}')
elif sign == '/':
    if num_2 == 0:
        print('Деление на ноль запрещено')
    else:
        print(f'{num_1 / num_2:.2f}')
else:
    print('Неизвестная операция')
