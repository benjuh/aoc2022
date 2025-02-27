from util.files import *
from util.runner import *
import time

TESTING = False
lines = GetLines(6, TESTING)

def part1():
    processed = 3
    for line in lines:
        chars = set()
        for i in range(len(line)):
            chars = set(line[i:i+4])
            processed += 1
            if len(chars) == 4:
                break
    return processed

def part2():
    processed = 13
    for line in lines:
        chars = set()
        for i in range(len(line)):
            chars = set(line[i:i+14])
            processed += 1
            if len(chars) == 14:
                break
    return processed


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(6, ans1, ans2, time1, time2)
