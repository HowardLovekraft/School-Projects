for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = not((x <= y) <= w) and z
                if f == 1:
                    print(w, y, x, z)
