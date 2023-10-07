for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = x <= y or not(w <= z)
                if f == 0:
                    print(z, y, w, x, f)