n, w, h = [*map(int, input().split())]
cood = [[i + 1, *map(int, input().split())] for i in range(n)]
cood = [[0, w,h], *cood]

xs = sorted(set(map(lambda co:co[1], cood)))
ys = sorted(set(map(lambda co:co[2], cood)))
cood = sorted([[i, xs.index(x), ys.index(y)] for i, x, y in cood], key=lambda co:co[1])
dp = [[0] * len(xs) for _ in range(len(ys))]
print(*dp, sep='\n')
print(cood)