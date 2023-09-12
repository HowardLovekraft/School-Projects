for n in range(1000, 10000):
    num = str(n)
    s1 = int(num[0]) + int(num[1])
    s2 = int(num[2]) + int(num[3])
    if s1 > s2:
        s3 = str(s1) + str(s2)
    else:
        s3 = str(s2) + str(s1)
    if s3 == "1311":
        print(num)
        break

# 2949
