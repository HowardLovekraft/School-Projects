# Вариант 4
string = "22" + "1"*2023
while "2111" in string or "1112" in string:
    string = string.replace("111", "1", 1)
    if "21" in string:
        string = string.replace("21", "12", 1)
    else:
        string = string.replace("12", "1", 1)
print(string)
