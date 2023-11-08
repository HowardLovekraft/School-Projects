for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (w <= y) and (not(y) == x) and (x or z):
                    print(x, z, w, y)