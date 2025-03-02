from util.files import *
from util.runner import *
import time

from itertools import cycle
key = 811589153

TESTING = False

lines = GetLines(20, TESTING)
def part1():
    rounds, mutliply = (1, 1)
    numbers = [int(n) * mutliply for n in lines]
    mixed = [a for a in enumerate(numbers)]
    cyc = cycle(mixed.copy())
    zero_tuple = (numbers.index(0), 0)
    lm = len(mixed) - 1

    for _ in range(rounds * len(numbers)):
        curr = next(cyc)
        idx_old = mixed.index(curr)
        mixed.remove(curr)
        idx_new = (idx_old + curr[1] + lm) % lm
        mixed.insert(idx_new, curr)

    idx_zero_tuple = mixed.index(zero_tuple)
    return sum([mixed[(idx_zero_tuple + i) % len(numbers)][1]
          for i in [1000, 2000, 3000]])

def part2():
    rounds, mutliply = (10, key)
    numbers = [int(n) * mutliply for n in lines]
    mixed = [a for a in enumerate(numbers)]
    cyc = cycle(mixed.copy())
    zero_tuple = (numbers.index(0), 0)
    lm = len(mixed) - 1

    for _ in range(rounds * len(numbers)):
        curr = next(cyc)
        idx_old = mixed.index(curr)
        mixed.remove(curr)
        idx_new = (idx_old + curr[1] + lm) % lm
        mixed.insert(idx_new, curr)

    idx_zero_tuple = mixed.index(zero_tuple)
    return sum([mixed[(idx_zero_tuple + i) % len(numbers)][1]
          for i in [1000, 2000, 3000]])

    return 0


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(20, ans1, ans2, time1, time2)
