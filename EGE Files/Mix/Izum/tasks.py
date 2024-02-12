def num46_to_alt_view(base):
    NUM_STR = "46"
    NUM = 46
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
        NUM_BASE += str(tm)
    return NUM_BASE

for base in range(2, 100):
    num = num46_to_alt_view(base)
    print(base, num, "\t", len(num))