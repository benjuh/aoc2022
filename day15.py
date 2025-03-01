from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(15, TESTING)

def possible(x, y, sensors, beacons):
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True

def part1():
    sensors, beacons = parse(lines)
    ct = 0
    y = 2_000_000
    for x in range(min(x-d for x, _, d in sensors), max(x+d for x, _, d in sensors)):
        if not possible(x, y, sensors, beacons) and (x, y) not in beacons:
            ct += 1
    return ct

def part2():
    sensors, beacons = parse(lines)
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                x, y = sx + (dx * mx), sy + (dy * my)
                if not(0 <= 4_000_000 and 0<=y<=4_000_000):
                    continue
                if possible(x, y, sensors, beacons):
                    return x * 4_000_000 + y

def parse(lines):
    sensors, beacons = set(), set()
    for line in lines:
        parts = line.split()
        sx, sy = int(parts[2][2:-1]), int(parts[3][2:-1])
        bx, by = int(parts[8][2:-1]), int(parts[9][2:])
        d = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, d))
        beacons.add((bx, by))
    return sensors, beacons

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(15, ans1, ans2, time1, time2)
