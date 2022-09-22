def run_each(reader):
    n = int(reader())
    for i in range(n):
        run(reader)

def run_with(reader):
    def read_with():
        n = int(reader())
        if n == 0:
            return False, None
        c = []
        for i in range(n):
            pass
        return True, c

    more, c = read_with()
    while more:
        debug(*c, sep='\n')

        res = run(*c)
        print(res)

        more, c = read_with()

# Either or
# debug = print
debug = lambda *args, **kwargs: None

def run(reader):
    n = int(reader())
    a = [*map(int, reader().split())]
    d = [*map(int, reader().split())]
    out = [0] * n
    mingreater = [0] * n
    j = 0
    for i in range(n):
        while a[i] > d[j]:
            j += 1
        mingreater[i] = j
        out[i] = d[j]-a[i]
    print(*out)

    out = [0] * n
    occupied = [0] * n
    highest = n-1
    for i in range(n-1, 0-1, -1):
        out[i] = d[highest] - a[i]
        j = mingreater[i]
        while occupied[j] > 0:
            occupied[j] += 1
            j += occupied[j] - 1
        # occupy
        occupied[j] = 1
        while occupied[highest] > 0 and highest >= 0:
            highest -= 1
    print(*out)
    

# Either or
run_method = run_each
# run_method = run_with

# Either or
# with open(".in") as f:
#     run_method(f.readline)
run_method(input)


