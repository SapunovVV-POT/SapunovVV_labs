first = "2"#Вводится строкове значение, вместо int
second = "3"#тоже самое
print(first + second)
#Исправленный вариант
first = 2
second = 3
print(first + second)

#age = input("Возраст: ")
#по умолчения вводится тип str, а для задачи необходим int
age=int(input("Возраст: "))
print(age + 1)

first = 4
second = 7
third = 10
#average = first + second + third / 3
#... ... скобочки
average = (first + second + third) / 3
print(average)
