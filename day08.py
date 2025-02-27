from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(8, TESTING)

grid = []
def parse(lines):
    grid.clear()
    for line in lines:
        row = []
        for char in line:
            val = int(char)
            row.append(val)
        grid.append(row)
    return

def transpose(grid):
    l = list(zip(*grid))
    return [list(x) for x in l]

def check_visibility(tree_x, tree_y, tree_height, transposed, grid):
    found_at_left_edge = True
    for _, height in enumerate(grid[tree_y][:tree_x]):
        if height >= tree_height:
            found_at_left_edge = False
            break
    if found_at_left_edge:
        return True
    found_at_right_edge = True
    for _, height in enumerate(grid[tree_y][tree_x+1:]):
        if height >= tree_height:
            found_at_right_edge = False
            break
    if found_at_right_edge:
        return True
    found_at_top_edge = True
    for _, height in enumerate(transposed[tree_x][tree_y+1:]):
        if height >= tree_height:
            found_at_top_edge = False
            break
    if found_at_top_edge:
        return True
    found_at_bottom_edge = True
    for _, height in enumerate(transposed[tree_x][:tree_y]):
        if height >= tree_height:
            found_at_bottom_edge = False
            break
    if found_at_bottom_edge:
        return True

    return False

def scenic_score(tree_x, tree_y, tree_height, transposed, grid):
    left_tallest = tree_height
    left_score = 0
    for _, height in enumerate(grid[tree_y][:tree_x]):
        left_score += 1
        if height < left_tallest:
            left_tallest = height
        else:
            break
            
    right_tallest = tree_height
    right_score = 0
    for _, height in enumerate(grid[tree_y][tree_x+1:]):
        right_score += 1
        if height < right_tallest:
            right_tallest = height
        else:
            break
        
    top_tallest = tree_height
    top_score = 0
    for _, height in enumerate(transposed[tree_x][tree_y+1:]):
        top_score += 1
        if height < top_tallest:
            top_tallest = height
        else:
            break
    
    bottom_tallest = tree_height
    bottom_score = 0
    for _, height in enumerate(transposed[tree_x][:tree_y]):
        bottom_score += 1
        if height < bottom_tallest:
            bottom_tallest = height
        else:
            break
    
    return left_score * right_score * top_score * bottom_score

def part1():
    parse(lines)
    visible = 0
    transposed = transpose(grid)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if x == 0 or y == 0 or x == len(row) - 1 or y == len(grid) - 1:
                visible += 1
                continue
            if check_visibility(x, y, val, transposed, grid):
                visible += 1

    return visible

def hike(y, x, grid):
    currentNum = grid[y][x]
    Up = 0
    Down = 0
    Left = 0
    Right = 0
    for left in range(x -1, -1, -1):
        Left += 1
        if grid[y][left] >= currentNum:
            break
    for right in range(x + 1, len(grid[y])):
        Right += 1
        if grid[y][right] >= currentNum:
            break
    for up in range(y - 1, -1, -1):
        Up += 1
        if grid[up][x] >= currentNum:
            break
    for down in range(y + 1, len(grid)):
        Down += 1
        if grid[down][x] >= currentNum:
            break
    return Up * Down * Left * Right
    

def part2():
    parse(lines)
    top_score = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            score = hike(y, x, grid)
            top_score = max(top_score, score)

    return top_score


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(8, ans1, ans2, time1, time2)
