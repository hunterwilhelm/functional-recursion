import timeit
from functional_recursion import recur_yield, tail_recursive_yield

def fib_standard_recursive(last_two=None):
    if last_two is None:
        last_two = (0, 1)
    yield last_two[0]
    next_two = (last_two[1], sum(last_two))
    yield from fib_standard_recursive(next_two)


def fib_standard_loop():
    last_two = (0, 1)
    while True:
        yield last_two[0]
        last_two = (last_two[1], sum(last_two))


@tail_recursive_yield
def fib_decorator_recursive(last_two=None):
    if last_two is None:
        last_two = (0, 1)
    last_two = (last_two[1], sum(last_two))
    return recur_yield(last_two, yield_val=last_two[0])


def print_last(generator, count):
    fib_num = 0
    for _ in range(count):
        fib_num = next(generator)
    number_of_digits = len(str(fib_num))
    print(f"> the last digit generated has {number_of_digits} digits")


def log_time(message, func, count):
    print(">>", message)
    try:
        total_time = timeit.timeit(lambda: print_last(func(), count), number=1)
        print(f"> {total_time:.3} seconds\n")
    except RecursionError as e:
        print("> " + repr(e) + "\n")


if __name__ == "__main__":
    print("100th fibonacci number".center(80, "="))
    log_time("fib_standard_recursive", fib_standard_recursive, 100)
    log_time("fib_standard_loop", fib_standard_loop, 100)
    log_time("fib_decorator_recursive", fib_decorator_recursive, 100)
    input("Press enter to continue")

    print("1000th fibonacci number".center(80, "="))
    log_time("fib_standard_recursive", fib_standard_recursive, 1000)
    log_time("fib_standard_loop", fib_standard_loop, 1000)
    log_time("fib_decorator_recursive", fib_decorator_recursive, 1000)
    input("Press enter to continue")

    print("100,000th fibonacci number".center(80, "="))
    log_time("fib_standard_recursive", fib_standard_recursive, 100_000)
    log_time("fib_standard_loop", fib_standard_loop, 100_000)
    log_time("fib_decorator_recursive", fib_decorator_recursive, 100_000)
    input("Press enter to continue")

    print("500,000th fibonacci number".center(80, "="))
    log_time("fib_standard_recursive", fib_standard_recursive, 500_000)
    log_time("fib_standard_loop", fib_standard_loop, 500_000)
    log_time("fib_decorator_recursive", fib_decorator_recursive, 500_000)
    input("Press enter to continue")

    print("1,000,000th fibonacci number".center(80, "="))
    log_time("fib_standard_recursive", fib_standard_recursive, 1_000_000)
    log_time("fib_standard_loop", fib_standard_loop, 1_000_000)
    log_time("fib_decorator_recursive", fib_decorator_recursive, 1_000_000)
    input("Press enter to continue")
