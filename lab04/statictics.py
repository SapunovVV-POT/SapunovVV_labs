n=int(input("Введите число >=1:"))
a=int(input("Введите число:"))
sum_n=a
n_positive=0
if (a>0):
    n_positive=n_positive+1
max_n=a
for i in range(n-1):
    a=int(input("Введите число:"))
    sum_n=sum_n+a
    if (a>0):
        n_positive=n_positive+1
    if (a>max_n):
        max_n=a
print("Сумма всех чисел: ",sum_n)
print("Количиство положительных: ",n_positive)
print("Максимальное число: ", max_n)
