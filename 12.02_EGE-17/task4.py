file = tuple(int(j) for j in open("17(7).txt").readlines())

max_sqr = max(k for k in file if k % 10 == 3)**2
cnt = 0
max_sum = -float("INF")

for i in range(len(file)-1):
    a = file[i]
    b = file[i+1]

    a_2 = a**2
    b_2 = b**2
    if (a % 10 == 3 + b % 10 == 3) == 1 and ((a_2 + b_2) >= max_sqr):
        cnt += 1
        max_sum = max(max_sum, a_2 + b_2)

print(cnt, max_sum)
