# Вариант 8
x = "1"*65
while "11111" in x or "15" in x:
    if "11111" in x:
        x = x.replace("11111", "15", 1)
    else:
        x = x.replace("15", "1", 1)
print(x)
