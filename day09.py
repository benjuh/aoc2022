from util.files import *
from util.runner import *
import numpy as np
import time

TESTING = False

lines = GetLines(9, TESTING)

def solve(length):
    knots = [(0,0) for _ in range(length)]
    visited = set()
    visited.add(knots[-1])
    for line in lines:
        sections = line.split(" ")
        direction = sections[0]
        steps = int(sections[1])
        for _ in range(steps):
            match direction:
                case "U":
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case "D":
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                case "R":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                case "L":
                    knots[0] = (knots[0][0] - 1, knots[0][1])
            for k in range(length - 1):
                dx = knots[k][0] - knots[k + 1][0]
                dy = knots[k][1] - knots[k + 1][1]
                if abs(dx) > 1 or abs(dy) > 1:
                    knots[k+1] = (knots[k+1][0] + np.sign(dx), knots[k+1][1] + np.sign(dy))
                visited.add(knots[-1])
    return len(visited)

def part1():
    length = 2
    return solve(length)

def part2():
    length = 10
    return solve(length)


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(9, ans1, ans2, time1, time2)
