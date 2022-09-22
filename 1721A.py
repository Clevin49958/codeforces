n = int(input())
for i in range(n):
    line = input()+input()
    d = {}
    for char in line:
        if char in d:
            d[char]+=1
        else:
            d[char] = 1
    counts = sorted(d.values(), reverse=True)
    if counts[0] == 4:
        print(0)
    elif counts[0] == 3:
        print(1)
    elif counts[0] == 1:
        print(3)
    # 2xx
    elif counts[1] == 2:
        print(1)
    else:
        print(2)
    # print(counts)