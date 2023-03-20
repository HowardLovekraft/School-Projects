# Решение для 2 задачи
'''for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (((x and not(y)) == (z or not(w))) <= (x and z)) == 0:
                    print(x, y, z, w)'''


# Решение для 6 задачи
'''использовать Черепаха
алг
нач
    опустить хвост
    нц 5 раз
        вперед(7)
        вправо(90)
        вперед(4)
        вправо(90)
    кц
кон'''


# Решение для 14 задачи
'''def changer(s):
    if s == 10:
        s == "A"
    elif s == 11:
        s == "B"
    elif s == 12:
        s == "C"

for x in range(0, 12):
    for y in range(0, 12):
        changer(x)
        changer(y)
        ans = int(str(y) + "AA" + str(x), 12)
        ans2 = int(str(x) + "02" + str(y), 14)
        res = ans + ans/2
        if res % 80 == 0:
            print(x, y, res/80)'''
