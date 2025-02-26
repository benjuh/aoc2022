from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(4, TESTING)

pairs = []
def parse():
    pairs.clear()
    for line in lines:
        lr = line.split(",")
        left = lr[0].split("-")
        right = lr[1].split("-")
        pairs.append((int(left[0]), int(left[1]), int(right[0]), int(right[1])))
    return
def containsOther(start1, end1, start2, end2):
    if start1 >= start2 and start1 <= end2 and end1 >= start2 and end1 <= end2:
        return True
    if start2 >= start1 and start2 <= end1 and end2 >= start1 and end2 <= end1:
        return True
    return False

def overlaps(start1, end1, start2, end2):
    if start1 >= start2 and start1 <= end2:
        return True
    if start2 >= start1 and start2 <= end1:
        return True
    if end1 >= start2 and end1 <= end2:
        return True
    if end2 >= start1 and end2 <= end1:
        return True
    return False

def part1():
    parse()
    total = 0
    for (start1, end1, start2, end2) in pairs:
        if containsOther(start1, end1, start2, end2):
            total += 1

    return total

def part2():
    parse()
    total = 0
    for (start1, end1, start2, end2) in pairs:
        if overlaps(start1, end1, start2, end2):
            total += 1
    return total


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(4, ans1, ans2, time1, time2)
