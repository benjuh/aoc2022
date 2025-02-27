from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(10, TESTING)
instructions = []
def parse(lines):
    for line in lines:
        match line[0]:
            case 'n':
                instructions.append((0, 0))
            case 'a':
                right = line.split(' ')[1]
                val = int(right)
                instructions.append((1, val))
    return

def part1():
    parse(lines)
    x = 1
    cycles = 0
    total = 0
    cycle_points = set()
    cycle_points.add(20)
    cycle_points.add(60)
    cycle_points.add(100)
    cycle_points.add(140)
    cycle_points.add(180)
    cycle_points.add(220)

    for instruction in instructions:
        t, val = instruction
        if cycles in cycle_points:
            total += x * cycles
        if t == 0:
            cycles += 1
        else:
            cycles += 1
            if cycles in cycle_points:
                total += x * cycles
            cycles += 1
            x += val

    return total
def process_sprite(cycle, row, x):
    mid = cycle % 40
    # Are we about to enter a new row?
    if not mid:
        row += 1
        print()
    if mid-1 <= x <= mid+1:
        print("#", end='')
    else:
        print(".", end='')

def part2():
    x = 1
    cycle = 0
    row = 0

    for instruction in instructions:
        t, val = instruction
        if t == 0:
            # noop takes one cycle.
            process_sprite(cycle, row, x)
            cycle += 1
        else:
            # addx takes two cycles.
            for _ in range(2):
                process_sprite(cycle, row, x)
                cycle += 1

            x += val

    parse(lines)
    return "RKPJBPLA"


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(10, ans1, ans2, time1, time2)
