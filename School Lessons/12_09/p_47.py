def ten_to_hex(number):
    if number == 10:
        return 'A'
    elif number == 11:
        return 'B'
    elif number == 12:
        return 'C'
    elif number == 13:
        return 'D'
    elif number == 14:
        return 'E'
    elif number == 15:
        return 'F'
    else:
        return str(number)

res = []
for a in range(1, 16):
    for b in range(1, 16):
        for c in range(1, 16):
            a_hex, b_hex, c_hex = ten_to_hex(a), ten_to_hex(b), ten_to_hex(c)
            a_ten, b_ten, c_ten = int(a_hex, 16), int(b_hex, 16), int(c_hex, 16)
            r1 = a_ten - b_ten
            r2 = b_ten - c_ten
            if r2 <= r1:
                res.append(str(r1) + str(r2))
            else:
                res.append(str(r2) + str(r1))

if "131" in res:
    print("131 в списке")
elif "133" in res:
    print("133 в списке")
elif "212" in res:
    print("212 в списке")
# D1 не может быть в списке, т.к. разности должны быть записаны в десятичной системе 
# счисления, соответственно цифры D в записи друг за другом быть не может

# 131 в списке
