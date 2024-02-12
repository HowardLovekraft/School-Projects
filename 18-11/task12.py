import random
rand = random.Random()
res = []
for n in range(2):
    s_s = list("1" * 11 + "2" * n + "3" * 11)
    rand.shuffle(s_s)
    s = ">" + "".join(s_s)

    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "222>", 1)
        if ">2" in s:
            s = s.replace(">2", "3>", 1)
        if ">3" in s:
            s = s.replace(">3", "1>", 1)
    while ">" in s or "<" in s:
        s = s.replace(">", "", 1)
        s = s.replace("<", "", 1)

    s_sum = [int(x) for x in s]
    print(s_sum, sum(s_sum))