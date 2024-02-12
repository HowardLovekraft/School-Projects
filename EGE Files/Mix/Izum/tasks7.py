for n in range(1000):
    n_bin = bin(n)[2:]
    len_n = n_bin.count("1")
    n_bin += str(len_n % 2)
    len_n = n_bin.count("1")
    n_bin += str(len_n % 2)

    if int(n_bin, 2) > 60:
        print(n, n_bin, int(n_bin, 2))
        break