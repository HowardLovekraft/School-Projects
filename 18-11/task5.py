ans = []
for n in range(0, 300):
    n_bin = list(bin(n)[2::])
    for i in range(len(n_bin)):
        if n_bin[i] == '0':
            n_bin[i] = "01"
        elif n_bin[i] == "1":
            n_bin[i] = "10"
    r = int("".join(n_bin), 2)
    if r > 256:
        break
    else:
        ans.append(r)
print(ans)
