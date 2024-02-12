file = tuple(int(j) for j in open("17(3).txt").readlines())

file_2 = tuple(k for k in file if k % 2 == 1)
avg = sum(file_2) / len(file_2)
cnt = 0
max_sum = -1

for i in range(len(file)-1):
    a = file[i]
    b = file[i+1]
    if (a % 5 == 0 or b % 5 == 0) and \
       (a < avg or b < avg):
        cnt += 1
        max_sum = max(max_sum, a+b)

print(cnt, max_sum)