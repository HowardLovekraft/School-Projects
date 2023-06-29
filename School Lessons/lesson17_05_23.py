
# Задание 2
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not (y and (not x)) and not(x == z) and w) == 1:
                    print(y, x, z, w)


# Задание 5
for n in range(4, 100):
    s = bin(n)[2:]
    s = str(s)
    if n % 3 == 0:
        s += s[-3:]
    elif n % 3 != 0:
        ost = (n % 3) * 3
        ost2 = bin(ost)[2:]
        s += ost2
    r = int(s, 2)
    if r > 76:
        print(n)
        break


# Задание 14
for x in range(0, 10):
    first = int(f"97968{x}15", 15)
    second = int(f"7{x}233", 15)

    sum = first + second
    if sum % 14 == 0:
        print(x)
        break

# получаем x = 5
first = int(f"97968515", 15)
second = int(f"75233", 15)

sum = first + second
sum = sum // 14
print(sum)


# задание 16
def F(n):
    if n >= 2025:
        return n
    elif n < 2025:
        return n + F(n+2)

print(F(2022) - F(2023))
