s = 4**2022 - 2*4**1111 + 16**600 + 192
cnt = 0
while s > 0:
    if s % 4 == 3:
        cnt += 1
    s //= 4
print(cnt)