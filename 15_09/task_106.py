ans = []
for x in range(10, 100):
    a = x % 4
    b = x % 2
    c = x % 5
    res = f"{a}{b}{c}"
    if res == "202":
        ans.append(x)
print(max(ans))

# Ответ: 82
