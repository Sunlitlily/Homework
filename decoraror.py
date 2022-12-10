def my_decorator(func, N=3, K=3):
    memory = {}
    result = {}

    def decorated(*p):
        if N == None:
            return func(*p)
        if p in memory:
            memory[p] += 1
            return result[p]
        elif len(memory) < N or N == -1:
            memory[p] = 1
            result[p] = func(*p)
        else:
            out = min(memory.values())
            for r in result:
                if memory[r] == out:
                    result.pop(r)
                    break
            for m in memory:
                if memory[m] == out:
                    memory.pop(m)
                    break
            memory[p] = 1
            result[p] = func(*p)
        return func(*p)

    return decorated


import time


def clock(func):
    def clocked(*args):
        t_start = time.time()
        res = func(*args)
        total_time = time.time() - t_start

        print(f'{func.__name__}({args}) -> {res} executed in {total_time:.3f}s')

        return res

    return clocked


import random


@clock
def do_heavy_calculation(*args):
    time.sleep(2)
    ans = random.randint(1, 5)
    return ans


def clock2(func):
    @my_decorator
    def clocked(*args):
        t_start = time.time()
        res = func(*args)
        total_time = time.time() - t_start

        print(f'{func.__name__}({args}) -> {res} executed in {total_time:.3f}s')

        return res

    return clocked


do_heavy_calculation(1, 2, 3)
do_heavy_calculation(1, 2, 3)
do_heavy_calculation(5, 6, 3)
do_heavy_calculation(2, 5, 7)
do_heavy_calculation(1, 2, 3)
do_heavy_calculation(5, 6, 3)
do_heavy_calculation(4, 7, 8)
do_heavy_calculation(1, 2, 3)
do_heavy_calculation(5, 6, 9)
do_heavy_calculation(5, 6, 3)
do_heavy_calculation(1, 5, 7)
print('...')


@clock2
def do_heavy_calculation(*args):
    time.sleep(2)
    ans = random.randint(1, 5)
    return ans


do_heavy_calculation(1, 2, 3)
do_heavy_calculation(1, 2, 3)
do_heavy_calculation(5, 6, 3)
do_heavy_calculation(2, 5, 7)
do_heavy_calculation(1, 2, 3)
do_heavy_calculation(5, 6, 3)
do_heavy_calculation(4, 7, 8)
do_heavy_calculation(1, 2, 3)
do_heavy_calculation(5, 6, 9)
do_heavy_calculation(5, 6, 3)
do_heavy_calculation(1, 5, 7)
print('...')
