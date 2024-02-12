'''
Укажите числами через запятую и без пробелов в порядке возрастания все
основания систем счисления, в которых
запись числа 29 оканчивается на 5
'''

def num29_to_alt_view(base):
    NUM_STR = "29"
    NUM = 29
    NUM_BASE = ""
    for dec in NUM_STR:
        tms = 0
        while base**tms <= NUM:
            tms += 1
        tms -= 1 # cuz this works in this way, fuck out
        tm = 0
        while tm*base**tms <= NUM:
            tm += 1
        tm -= 1
        NUM -= tm*base**tms
        NUM_BASE += str(tm) + ' '
    return NUM_BASE

for base in range(6, 100):
    print(base, num29_to_alt_view(base))

'''
4 штуки!!! 
6 4 5 CHECKED
7 4 1        
8 3 5 CHECKED
9 3 2 
10 2 9 
11 2 7 
12 2 5 CHECKED 
13 2 3 
14 2 1 
15 1 14 
16 1 13 
17 1 12 
18 1 11 
19 1 10 
20 1 9 
21 1 8 
22 1 7 
23 1 6 
24 1 5 CHECKED 
25 1 4 
26 1 3 
27 1 2 
28 1 1 
29 1 0 
30 29 0
    ...
'''