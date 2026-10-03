surname=input("Введите фамилию: ")
name=input("Введите имя: ")
group=input("Введите группу: ")
city=input("Введите город: ")
age=int(input("Введите возраст в полных годах (от 1 до 120): "))
like_subject=input("Введите любимый предмет: ")
hours_per_week=float(input("Введите количество часов подготовки в неделю: "))

future_age=age + 4
prep_four_weeks=hours_per_week * 4
avg_prep_per_day=hours_per_week / 7

print("Карточка профиля: ")
print(f"Полное имя: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст через 4 года: {future_age}")
print(f"Любимый предмет: {like_subject}")
print(f"Время подготовки за четыре недели: {prep_four_weeks:.2f}")
print(f"Среднее время подготовки в день: {avg_prep_per_day:.2f}")
