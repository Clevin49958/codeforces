n, w, h = [*map(int, input().split())]
cood = [[*map(int, input().split())] for _ in range(n)]
# cood = filter(lambda co: co[0] > w and co[1] > h, cood)
cood = [[w,h], *cood]
n += 1
count = [0] * n
paths = [0] * n
for i in range(n):
    for j in range(n):
        if i != j:
            if cood[i][0] < cood[j][0] and cood[i][1] < cood[j][1]:
                if count[j] - 1 < count[i]:
                    count[j] = count[i] + 1
                    paths[j] = i

print(max(count))
index= count.index(max(count))
indexes = [index]
while index != 0:
    indexes.append(paths[index])
    index = paths[index]
print(*reversed(indexes[:-1]))
