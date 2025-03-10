from util.files import *
from util.runner import *
import time
import numpy as np

TESTING = False

lines = GetLines(14, TESTING)

ROCK = '#'
SAND = 'o'
AIR = '.'

def parse(lines):
    cave = np.full((318, 1000), '.')
    bottom_depth = 0
    for s in lines:
        path = s.split(' -> ')
        for i in range(0, len(path) - 1):
            p1, p2 = path[i].split(','), path[i + 1].split(',')
            x1, y1 = int(p1[0]), int(p1[1])
            x2, y2 = int(p2[0]), int(p2[1])
            points = points_on_line(x1, y1, x2, y2)
            for (x, y) in points:
                cave[y, x] = ROCK
                bottom_depth = max(y, bottom_depth)

    return cave, bottom_depth

def points_on_line(x1, y1, x2, y2):
    xrange = range(x1, x2 + 1) if x2 >= x1 else range(x2, x1 + 1)
    yrange = range(y1, y2 + 1) if y2 >= y1 else range(y2, y1 + 1)
    return [(x, y) for x in xrange for y in yrange]



def part1():
    input, bottom_depth = parse(lines)
    sand_count = 0
    cave = input.copy()

    while True:
        sand_count += 1
        r, c = 0, 500
        while True:
            if r > bottom_depth:
                return sand_count - 1
            elif cave[r + 1, c] == AIR:
                r += 1
            elif cave[r + 1, c - 1] == AIR:
                r += 1
                c -= 1
            elif cave[r + 1, c + 1] == AIR:
                r += 1
                c += 1
            else:
                cave[r, c] = SAND
                break


def part2():
    input, bottom_depth = parse(lines)
    sand_count = 0
    cave = input.copy()
    floor_depth = bottom_depth + 2

    while True:
        sand_count += 1
        r, c = 0, 500
        while True:
            if r + 1 >= floor_depth:
                cave[r, c] = SAND
                break
            elif cave[1, 499] == cave[1, 500] == cave[1, 501] == SAND:
                # draw(cave)
                return sand_count
            elif cave[r + 1, c] == AIR:
                r += 1
            elif cave[r + 1, c - 1] == AIR:
                r += 1
                c -= 1
            elif cave[r + 1, c + 1] == AIR:
                r += 1
                c += 1
            else:
                cave[r, c] = SAND
                break


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(14, ans1, ans2, time1, time2)
