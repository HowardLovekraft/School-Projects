# Вариант 9
x = "1"*70
while "1111" in x or "2222" in x:
    if "1111" in x:
        x = x.replace("1111", "22", 1)
    else:
        x = x.replace("2222", "11", 1)
print(x)
