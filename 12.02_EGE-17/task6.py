file = tuple(int(k) for k in open("17(9).txt").readlines())

cnt = 0
max_sum = -1

for i in range(len(file)-1):
    for j in range(i+1, len(file)):
        a = file[i]
        b = file[j]

        if ((a+b) % 2 != 0) and ((a*b) % 5 == 0):
            cnt += 1
            max_sum = max(max_sum, a+b)

print(cnt, max_sum)