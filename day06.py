from util.files import *
from util.runner import *
import time

TESTING = True

lines = GetLines(6, TESTING)
PrintLines(lines)
def parse():
    _ = lines
    return

def part1():
    parse()
    return 0

def part2():
    parse()
    return 0


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(6, ans1, ans2, time1, time2)
