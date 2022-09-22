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

# Either or
run_method = run_each
# run_method = run_with

# Either or
with open(".in") as f:
    run_method(f.readline)
# run_method(input)


