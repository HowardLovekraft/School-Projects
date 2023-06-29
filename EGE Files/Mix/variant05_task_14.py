x = 5**20222 - 2*5**1010 + 25**850 + 2500
cnt = 0
while x > 0:
    if x % 5 == 4:
        cnt += 1
    x //= 5
print(cnt)