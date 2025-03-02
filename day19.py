from util.files import *
from util.runner import *
import time
import re
import numpy as np

TESTING = False

V = lambda *a: np.array(a)
key = lambda a: tuple(a[0]+a[1]) + tuple(a[1])
prune = lambda x: sorted({key(x):x for x in x}.values(), key=key)[-1000:]

lines = GetLines(19, TESTING)

def parse(line):
    i,a,b,c,d,e,f = map(int, re.findall(r'\d+',line))
    return (i, (V(0,0,0,a), V(0,0,0,1)),
               (V(0,0,0,b), V(0,0,1,0)),
               (V(0,0,d,c), V(0,1,0,0)),
               (V(0,f,0,e), V(1,0,0,0)),
               (V(0,0,0,0), V(0,0,0,0)))
def run(blueprint, t):
    todo = [(V(0,0,0,0), V(0,0,0,1))]
    for _ in range(t,0,-1):
        todo_ = list()
        for have, make in todo:
            for cost, more in blueprint:
                if all(cost <= have):
                    todo_.append((have+make-cost, make+more))
        todo = prune(todo_)
    return max(have[0] for have, _ in todo)

def part1():
    total = 0
    for i, *blueprint in map(parse, lines):
        total += run(blueprint, 24) * i
    return total

def part2():
    total = 1
    for i, *blueprint in map(parse, lines):
        total *= run(blueprint, 32) if i<4 else 1
    return total


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(19, ans1, ans2, time1, time2)
