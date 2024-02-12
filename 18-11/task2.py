def imp(x, y):
    return not(x) or y

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(imp(x, y)) or imp(not w, not z) or w
                if not f:
                    print(x, y, z, w)