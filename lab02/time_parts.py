total_seconds=int(input("Введите число больше 0: "))

hours=total_seconds//3600
new_total_seconds=total_seconds%3600
minutes=new_total_seconds//60
seconds=new_total_seconds%60

print(f"{hours} ч,{minutes} м, {seconds} с.")
