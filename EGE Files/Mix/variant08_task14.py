s = 3**2021 + 5*3**2000 + 3**501 + 5*3**500 + 1
cnt = 0
while s > 0:
    if s % 9 == 0:
        cnt += 1
    s //= 9
print(cnt)