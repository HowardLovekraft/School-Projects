for A in range(100):
    flag = True
    for x in range(150):
        for y in range(150):
            if not(((2*x + 3*y) != 60) or (A >= x) or (A >= y)):
                flag = False
    if flag == True:
        print(A)
        break
    
