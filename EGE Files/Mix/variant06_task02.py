for x in range(0, 2):
    for w in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = ((z <= y) <= x) or (not w)
                if f == 0:
                    print(w, y, z, x)