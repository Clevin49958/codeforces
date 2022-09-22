import math


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
    pass

def build_dp(n, dishes):
    dpa = [0]
    dpb = [0] * 2
    # black red
    for i in range(1, n+1):
        dpb[0] = dpa[0] + dishes[i-1][0]
        dpb[-1] = dpa[-1] + dishes[i-1][1]
        for x in range(1, i):
            y = i-x
            dpb[x] = max(dpa[x] + dishes[i-1][0], dpa[x-1] + dishes[i-1][1])
            pass
        dpa = dpb
        dpb = [0] * (i + 2)
    return dpa
def runner_wrapper(reader):
    n = int(reader())
    dishes = [[*map(int, reader().split())] for _ in range(n)]

    dp = build_dp(n, dishes)
    
    m = int(reader())
    debug(*dp, sep='\n')
    for i in range(m):
        shop = [*map(int, reader().split())]
        lcm = math.lcm(shop)
        max_score = -1
        for black in range(0, n + 1, shop[0]):
            red = n - black
            if red % shop[1] != 0:
                continue
            if dp[red] > max_score:
                max_score = dp[red]
        print(max_score)
# Either or
run_method = runner_wrapper
# run_method = run_with

# Either or
# with open(".in") as f:
    # run_method(f.readline)
run_method(input)


