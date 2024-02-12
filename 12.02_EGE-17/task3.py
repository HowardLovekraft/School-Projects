file = tuple(int(j) for j in open("17(6).txt").readlines())

cnt = 0
max_sum = -1

for i in range(len(file)-1):
    for k in range(i+1, len(file)):
        a = file[i]
        b = file[k]

        if (a*b) % 26 == 0:
            cnt += 1
            max_sum = max(max_sum, a+b)

print(cnt, max_sum)