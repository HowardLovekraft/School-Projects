st = [1]

cur_st = [1]
for x in range(13 - 1):
    cur_st.append(sum(cur_st) % 13)

print(cur_st)
print(200 - (200 // 13 * 13), 99993 - (99993 // 13 * 13))

