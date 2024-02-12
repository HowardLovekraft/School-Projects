n = 5**28 + 25**6 - 125
cnt = 0
while n > 0:
    if n % 5 == 4:
        cnt += 1
    n //= 5
print(cnt)