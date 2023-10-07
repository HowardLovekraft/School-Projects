ex = 81**17 + 3**24 - 45
cnt = 0
while ex > 0:
    if ex%9 == 8:
        cnt += 1
    ex//= 9
print(cnt)