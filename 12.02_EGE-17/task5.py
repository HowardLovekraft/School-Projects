file = tuple(t.strip() for t in open("17(8).txt").readlines())
file_len = len(file)

max_elem = max((int(t) for t in file if t[-3:] == "321"))
max_sum = -float("INF")
cnt = 0

for i in range(file_len-2):
    a, b, c = file[i], file[i+1], file[i+2]

    eq_1 = tuple(len(m) for m in (a, b, c))
    if eq_1.count(5) == 2:
        if int(a) % 5 == 0 or \
            int(b) % 5 == 0 or int(c) % 5 == 0:
            summy = sum(int(m) for m in (a, b, c))
            if summy > max_elem:
                cnt += 1
                max_sum = max(summy, max_sum)

print(cnt, max_sum)