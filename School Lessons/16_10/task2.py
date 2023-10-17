for A in range(100):
    flag = True
    for x in range(150):
        for y in range(150):
            if not(((y + 2*x) < A) or (x > 15) or (y > 30)):
                flag = False
    if flag == True:
        print(A)
        break
    
