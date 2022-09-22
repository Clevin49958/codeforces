from heapq import heapify
import heapq


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

def count(x):
    return -(len(str(x)) - 1)
def run(reader):
    n = int(reader())
    xs = [*map(lambda x: -int(x), reader().split())]
    heapify(xs)
    ys = [*map(lambda x: -int(x), reader().split())]
    heapify(ys)
    total = 0
    while len(xs) > 0:
        if xs[0] == ys[0]:
            heapq.heappop(xs)
            heapq.heappop(ys)
        else:
            bigger_heap = xs if xs[0] < ys[0] else ys
            heapq.heapreplace(bigger_heap, count(bigger_heap[0]))
            total+=1
        pass
    print(total)
# Either or
run_method = run_each
# run_method = run_with

# Either or
# with open(".in") as f:
    # run_method(f.readline)
run_method(input)


