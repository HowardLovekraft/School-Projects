n = 25**40 - 5**30 + 24
cnt = 0
while n > 0:
    if n % 5 == 4:
        cnt += 1
    n//=5

print(cnt)