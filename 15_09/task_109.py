ans = []
for x in range(10, 100):
    a = x % 7
    b = x % 2
    c = x % 5
    res = f"{a}{b}{c}"
    if res == "312":
        ans.append(x)
print(len(ans))

# Ответ: 2
