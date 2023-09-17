ans = []
for x in range(10, 100):
    a = x % 4
    b = x % 3
    c = x % 2
    res = f"{a}{b}{c}"
    if res == "200":
        ans.append(x)
print(len(ans))

# Ответ: 7
