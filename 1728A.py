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
    n = int (reader())
    cnts = [*map(int, reader().split())]
    total = 0
    for i in range(n):
        ci = cnts[i]
        oc = [*cnts]
        oc.remove(ci)
        oc.sort()
        if len(oc)==0:
            print(i+1)
            break
        # start remove
        head = oc.pop()
        while len(oc) > 0:
            if head >= oc[-1]:
                head -= oc[-1]
                oc.pop()
            else:
                oc[-1] -= head
                head = oc.pop()
            debug("iter: ", head, oc)
        if ci > head:
            print(i+1)
            break
        debug(ci, oc, total)
    # print(total)
    pass

# Either or
run_method = run_each
# run_method = run_with

# Either or
# with open(".in") as f:
#     run_method(f.readline)
run_method(input)


