# list = []
# for x in range(1, 10**10):
#     x_bin = bin(x)[2:]
#     if len(str(x)) * 3 == len(x_bin):
#         list.append(x)
# print(list[10**8-685-1])
dt = {}
NUMBER = 10**8-685-1
prev_x = 2**3
for x in range(2**5, 2**100, 2**3):
    if prev_x < NUMBER < x:
        print(x, prev_x)
        break
    prev_x = x