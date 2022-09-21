from time import time


d, total = [*map(int, input().split())]
time_ranges = [[*map(int, input().split())] for i in range(d)]

t = [0] * d
lower = 0
upper = 0
for i in range(d):
    t[i] = time_ranges[i][0]
    lower += time_ranges[i][0]
    upper += time_ranges[i][1]

curr = lower
if total <= upper and total >= lower:
    for i in range(d):
        if curr < total:
            diff = time_ranges[i][1]-time_ranges[i][0]
            if curr + diff < total:
                curr += diff
            else:
                diff = total - curr
                curr = total
            t[i] += diff
    print("YES")
    print(*t)
else:
    print("NO")

