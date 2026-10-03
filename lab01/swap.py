first_room=input("Введите название аудитории: ")
second_room=input("Введите название другой аудитории: ")

print(f"Было: {first_room} --- {second_room}")

temp_room=second_room
second_room=first_room
first_room=temp_room

print(f"Стало: {first_room} --- {second_room}")
