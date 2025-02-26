from util.files import *
from util.runner import *
import time

TESTING = True

lines = GetLines(18, TESTING)
PrintLines(lines)
def parse(lines):
    _ = lines
    return

def part1():
    parse(lines)
    return 0

def part2():
    parse(lines)
    return 0


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(18, ans1, ans2, time1, time2)
