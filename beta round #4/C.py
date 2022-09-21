n = int(input())
names = {}
for i in range(n):
    name = input()
    if name in names:
        names[name] += 1
        print("%s%d" % (name, names[name]))
    else:
        print("OK")
        names[name] = 0