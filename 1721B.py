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
    n,m,x,y,d = [*map(int, reader().split())]
    r = x + d >= n
    l = x - d <= 1
    b = y + d >= m
    t = y-d <=1
    dist = n + m - 2
    if t and l or b and r or t and b or l and r:
        print(-1)
    else:
        print(dist)

# Either or
run_method = run_each
# run_method = run_with

# Either or
# with open(".in") as f:
#     run_method(f.readline)
run_method(input)


