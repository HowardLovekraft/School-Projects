ans = []
for x in range(10, 100):
    a = x % 4
    b = x % 2
    c = x % 3
    res = f"{a}{b}{c}"
    if res == "201":
        ans.append(x)
print(len(ans))

# Ответ: 8
