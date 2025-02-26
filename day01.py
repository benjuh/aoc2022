from util.files import *
from util.runner import *
import time
import queue
TESTING = False

lines = GetLines(1, TESTING)

def parse(lines):
    _ = lines
    return

def part1():
    parse(lines)
    most_calories = 0
    curr = 0
    for line in lines:
        if len(line) == 0:
            most_calories = max(most_calories, curr)
            curr = 0
            continue
        curr += int(line)
    return most_calories

def part2():
    parse(lines)
    q = queue.PriorityQueue()
    calories = 0
    for line in lines:
        if len(line) == 0:
            q.put((-calories, calories))
            calories = 0
            continue
        calories += int(line)
    elf1 = q.get()
    elf2 = q.get()
    elf3 = q.get()
    return elf1[1] + elf2[1] + elf3[1]

start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(1, ans1, ans2, time1, time2)
