from functools import cache
from itertools import permutations
# brute force
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

# @cache
def score(n):
    if n == 1:
        return 1, [1]
    max_score = 0
    max_perm = None
    for i in range(1, n):
        s, perm = score(i)
        if s < n and s > max_score:
            max_score = s
            max_perm = perm
    return max_score + n, [*max_perm, n]

def run(reader):
    n = int(reader())
    nums = [*range(1, n-1)]
    output = [0] * n
    output[-2] = n-1
    output[-1] = n
    if n % 2 == 1:
        output[0] = n-3
        output[1] = n-2
        output[2] = n-4
        for i in range(3, n-2):
            output[i] = n-i-2
    else:
        for i in range(n-2):
            output[i] = n-i-2
    print(*output)
# Either or
run_method = run_each
# run_method = run_with

# Either or
# with open(".in") as f:
    # run_method(f.readline)
run_method(input)


