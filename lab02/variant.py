#Вариант 3
total=int(input("Введите количество фотографий: "))
capacity=int(input("Введите количество фото на странице: "))

full_units=total//capacity
remainder=total%capacity
min_units=(total+capacity-1)//capacity

print("Количество полностью заполенных страниц: ", full_units)
print("Остаток: ", remainder)
print("Минимальное число страниц для размещения всего объема: ", min_units)
