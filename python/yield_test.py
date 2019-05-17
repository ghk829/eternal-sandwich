import contextlib

@contextlib.contextmanager
def yield_test():
    x = 0
    yield x
    x = 1
    print(x)

if __name__ == '__main__':
    with yield_test() as f:
        print(f)
    print(2)
