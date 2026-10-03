n=int(input("Введите число >=1:"))
n_condition=0
n_sum=0

for i in range(n):
    a=int(input("Введите число: "))
    if (10<=a<=20):
        n_condition=n_condition+1
        n_sum=n_sum+a

print("Количество числе удовлетворяющих условию: ",n_condition)
print("Сумма числе удовлетворяющих улсовию: ",n_sum)
