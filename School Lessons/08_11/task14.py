f = 4**12 + 2**32 - 16
cnt = 0
while f > 0:
    if f % 2 == 1:
        cnt += 1
    f //= 2
print(cnt)