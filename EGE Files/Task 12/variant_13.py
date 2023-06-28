# Вариант 13
x = "1" + "5"*25
while "15" in x or "1" in x:
    if "15" in x:
        x = x.replace("15", "5551", 1)
    else:
        if "1" in x:
            x = x.replace("1", "5", 1)
print(x.count("5"))
