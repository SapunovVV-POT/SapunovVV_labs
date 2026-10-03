sub_name_f=input("Введите название 1ого предмета: ")
sub_count_f=int(input("Введите количество занятий: "))
sub_duration_f=int(input("Введите продолжительность занятия: "))

sub_name_s=input("ВВедите название 2ого предмета: ")
sub_count_s=int(input("Введите количество занятий: "))
sub_duration_s=int(input("Введите продолжительность занятия: "))

total_hours_available=float(input("Введите свободное время: "))

sub_min_f=sub_count_f * sub_duration_f
sub_min_s=sub_count_s * sub_duration_s
total_load_min=sub_min_f + sub_min_s
total_load_hours=total_load_min / 60
free_hours=total_hours_available - total_load_hours
four_weeks_min=total_load_min * 4
four_weeks_hours=total_load_hours * 4

print(f"{sub_name_f}: {sub_min_f} мин")
print(f"{sub_name_s}: {sub_min_s} мин")
print(f"Общая нагрузка: {total_load_min} мин ({total_load_hours:.2f} ч)")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_min} мин ({four_weeks_hours:.2f} ч)")
