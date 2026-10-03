price=int(input("Введите цену одной тетради: "))
count=int(input("Введите количество тетрадей: "))
paid=int(input("Введите переданную сумму денег: "))

cost=price * count
change=paid - cost

if (change>=0):
    print(f"стоимость {cost}, сдача {change}")
else:
    print(f"Недостаточно средств")
