# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x <= y and (not z)) or w
#                 if f == False:
#                     print(x, w, z, y)

for i in range(100, 1000):
    i_list = [int(x) for x in str(i).split("")]
    i_copy = i_list.copy()
    