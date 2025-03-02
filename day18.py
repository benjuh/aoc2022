from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(18, TESTING)

def parse():
    cubes = []
    for line in lines:
        nums = line.split(",")
        cubes.append((int(nums[0]), int(nums[1]), int(nums[2])))

    minout = [min(c[i]-1 for c in cubes) for i in range(3)]
    maxout = [max(c[i]+1 for c in cubes) for i in range(3)]
    return cubes, minout, maxout

def in_space(cube, minout, maxout):
    return all(minout[i] <= cube[i] <= maxout[i] for i in range(3))


def get_neighbors(cube):
    return [tuple(sum(x) for x in zip(cube, d)) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]

def part1():
    cubes, _, _ = parse()
    exposed = 0
    for cube in cubes:
        for n in get_neighbors(cube):
            if n not in cubes:
                exposed += 1
    return exposed


def part2():
    cubes, minout, maxout = parse()
    exposed_outside = 0
    seen = set()
    queue = [tuple(maxout)]
    while queue:
        curr_cube = queue.pop(0)
        if curr_cube in cubes:
            exposed_outside += 1
            continue
        if curr_cube not in seen:
            seen.add(curr_cube)
            for n in get_neighbors(curr_cube):
                if in_space(n, minout, maxout):
                    queue.append(n)
    return exposed_outside


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(18, ans1, ans2, time1, time2)
