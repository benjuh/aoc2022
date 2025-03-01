from util.files import *
from util.runner import *
import time
from ast import literal_eval
from functools import cmp_to_key

path = "data/day13.txt"

with open(path) as f:
    content = [tuple(map(literal_eval, x)) for x in [a.split() for a in f.read().split("\n\n")]]

def com(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return com(a, b)
    
    a = [a] if isinstance(a, int) else a
    b = [b] if isinstance(b, int) else b

    a_list = len(a)
    b_list = len(b)
    min_list = min(a_list, b_list)

    for i in range(min_list):
        res = compare(a[i], b[i])
        if res == -1:
            return -1
        elif res == 1:
            return 1

    return com(a_list, b_list)


def part1():
    return sum(idx for idx, (p1, p2) in enumerate(content, start=1) if compare(p1, p2) == 1)

def part2():
    all = [[[2]], [[6]]]
    for t in content:
        all.extend(t)
    all = sorted(all, key=cmp_to_key(compare), reverse=True)
    return (all.index([[2]]) + 1) * (all.index([[6]]) + 1)


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(13, ans1, ans2, time1, time2)
