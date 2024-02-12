file = tuple(int(j) for j in open("17(4).txt").readlines())

avg_file = tuple(j for j in file if j % 2 == 0)
avg = sum(avg_file) / len(avg_file)
cnt = 0
max_sum = -1

for i in range(len(file)-1):
    a = file[i]
    b = file[i+1]
    if (a % 3 == 0 or b % 3 == 0) and (a < avg or b < avg):
        cnt += 1
        max_sum = max(max_sum, a+b)

print(cnt, max_sum)