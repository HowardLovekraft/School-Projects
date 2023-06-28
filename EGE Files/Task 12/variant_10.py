# Вариант 10
i = "2"*71
while "1111" in i or "2222" in i:
    if "1111" in i:
        i = i.replace("1111", "22", 1)
    else:
        i = i.replace("2222", "11", 1)
print(i)
