#Вариант 3
order_name=input("Название заказа: ")
c_name=input("Имя заказчика: ")

item_name_f=input("Введите название первой позиции: ")
item_n_f=int(input("Введите количество первой позиции: "))
item_price_f=float(input("Введите цену за едииницу товара первой позиции:"))

item_name_s=input("Введите название второй позиции: ")
item_n_s=int(input("Введите количество второй позиции: "))
item_price_s=float(input("Введите цену за едииницу товара второй позиции:"))

delivery_cost=float(input("Введите стоимость доставки: "))
paid=float(input("Введите внесенную сумму: "))
disc=int(input("Какая скидка в %"))

item_cost_f=item_n_f*item_price_f
item_cost_s=item_n_s*item_price_s
without_delivery=item_cost_f+item_cost_s
without_delivery_disc=(item_cost_f+item_cost_s)*(1-disc/100)
total=without_delivery_disc+delivery_cost
total_n=item_n_f+item_n_s
change=paid-total

print(f"Заказ: {order_name}")
print(f"Заказчик: {c_name}")
print("название | количество | цена | стоимость")
print(f"{item_name_f} | {item_n_f} | {item_price_f:.2f} | {item_cost_f:.2f}")
print(f"{item_name_s} | {item_n_s} | {item_price_s:.2f} | {item_cost_s:.2f}")
print(f"Стоимость товаров без доставки: {without_delivery:.2f}")
print(f"Стоимость товаров без доставки(с учетом скидки): {without_delivery_disc:.2f}")
print(f"Общая сумма с доставкой: {total:.2f}")
print(f"Общее количество единиц: {total_n}")
print(f"Сдача: {change:.2f}")
