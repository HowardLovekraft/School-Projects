res = []
for i in range(100, 1000):
    for j in range(100, 1000):
        i_str = str(i)
        j_str = str(j)
        fst_listed = [int(x) for x in list(i_str)]
        snd_listed = [int(x) for x in list(j_str)]
        sum_max_nums = max(fst_listed) + max(snd_listed)
        fst_listed.remove(max(fst_listed))
        snd_listed.remove(max(snd_listed))
        sum_avr_nums = max(fst_listed) + max(snd_listed)
        sum_min_nums = min(fst_listed) + min(snd_listed)

        if sum_max_nums > sum_avr_nums:
            res.append(str(sum_max_nums))
            if sum_avr_nums > sum_min_nums:
                res[-1] += str(sum_avr_nums)
                res[-1] += str(sum_min_nums)
            else:
                res[-1] += str(sum_min_nums)
                res[-1] += str(sum_avr_nums)
        else:
            res.append(str(sum_avr_nums))
            if sum_max_nums > sum_min_nums:
                res[-1] += str(sum_max_nums)
                res[-1] += str(sum_min_nums)
            else:
                res[-1] += str(sum_min_nums)
                res[-1] += str(sum_max_nums)

if "151303" in res:
    print("151303 is in the list")
elif "161410" in res:
    print("161410 is in the list")
elif "191615" in res:
    print("191615 is in the list")
elif "121613" in res:
    print("121613 is in the list")
