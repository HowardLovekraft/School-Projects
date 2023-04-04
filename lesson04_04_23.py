n = int(input("Введите число N: "))
score = 0
all = 0
print("Последовательно вводите номера имеющихся карточек:")
for i in range(n-1):
    score += int(input())
for i in range(1, n+1):
    all += i
print(f"Номер отсутствующей карточки - {all - score}")
