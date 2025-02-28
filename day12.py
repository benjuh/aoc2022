from util.files import *
from util.runner import *
import time
import collections

TESTING = False

lines = GetLines(12, TESTING)

start = []
end = []
grid = []
def parse(lines):
    start.clear()
    end.clear()
    grid.clear()
    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(line):
            val = line[x]
            if c == 'S':
                start.append((y, x))
                val = 'a'
            if c == 'E':
                end.append((y, x))
                val = 'z'
            elevation = ord(val) - ord('a')
            row.append(elevation)
        grid.append(row)
    return

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def hikeUp(source, dest):
    queue = collections.deque()
    visited = set()
    queue.append([source])
    while queue:
        path = queue.popleft()
        row, col = path[-1]
        elevation = grid[row][col]
        if (row, col) not in visited:
            visited.add((row, col))
            if (row, col) == dest:
                return len(path) - 1
            for dx, dy in directions:
                x = col + dx
                y = row + dy
                if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                    continue
            
                nh = grid[y][x]
                if nh <= elevation + 1:
                    path_copy = path[:]
                    path_copy.append((y, x))
                    queue.append(path_copy)
def hikeDown(dest):
    queue = collections.deque()
    visited = set()
    queue.append([dest])
    while queue:
        path = queue.popleft()
        row, col = path[-1]
        elevation = grid[row][col]
        if (row, col) not in visited:
            visited.add((row, col))
            if grid[row][col] == 0:
                return len(path) - 1
            for dx, dy in directions:
                x = col + dx
                y = row + dy
                if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                    continue
            
                nh = grid[y][x]
                if nh >= elevation - 1:
                    path_copy = path[:]
                    path_copy.append((y, x))
                    queue.append(path_copy)
                    
def part1():
    parse(lines)
    dist = hikeUp(start[0], end[0])
    return dist

def part2():
    parse(lines)
    dist = hikeDown(end[0])
    return dist


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(12, ans1, ans2, time1, time2)
