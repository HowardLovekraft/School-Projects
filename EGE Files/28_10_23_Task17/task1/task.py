file = open("17.txt", "r")
cache = []
def start_pair(cache):
    line = file.readline()
    cache.append(line)
def create_pair(cache):
    start_pair(cache)

    # benefits


cnt = 0
for line in file:
    if len(cache) == 0:
        cnt += 1
        start_pair(cache)
        continue
    elif len(cache) == 1:
        create_pair(cache)
    elif len(cache) > 2:
        cache.pop(0)
        cache.pop(0)
    else:
        print("Fuck!!!")
    print(cache)