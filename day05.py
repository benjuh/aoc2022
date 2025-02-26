from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLinesNoStrip(5, TESTING)

instructions = []
def parse():
    index_of_row = {}
    instructions.clear()
    line_of_width = 0
    for line in lines:
        if '[' not in line:
            break
        line_of_width += 1
    num_stacks = 0
    
    for i, char in enumerate(lines[line_of_width]):
        if char != ' ' and char != '\n' and char != '\r':
            num_stacks += 1
            index_of_row[i] = int(char) - 1

    stacks = [[] for _ in range(num_stacks)]
    for line in lines:
        for i, char in enumerate(line):
            if char == '[':
                row = index_of_row[i+1]
                contained = line[i+1:i+2]
                stacks[row].append(contained)

    line_of_instructions = line_of_width + 2
    for line in lines[line_of_instructions:]:
        instruction = []
        curr_number = None
        for char in line:
            if char == ' ' and curr_number is not None:
                instruction.append(int(curr_number))
                curr_number = None
                continue
            if char not in 'abcdefghijklmnopqrstuvwxyz ':
                if curr_number is not None:
                    curr_number += char
                elif curr_number is None:
                    curr_number = char
            elif char == ' ':
                curr_number = None
        if curr_number is not None:
            instruction.append(int(curr_number))
        instructions.append(instruction)
    for stack in stacks:
        stack.reverse()
    return stacks

def move(stacks, instruction):
    amount = instruction[0]
    src = instruction[1] - 1
    dest = instruction[2] - 1
    i = 0
    while i < amount and len(stacks[src]) > 0:
        stacks[dest].append(stacks[src].pop())
        i += 1

def move2(stacks, instruction):
    amount = instruction[0]
    src = instruction[1] - 1
    dest = instruction[2] - 1
    i = 0
    to_move = []
    while i < amount and len(stacks[src]) > 0:
        to_move.append(stacks[src].pop())
        i += 1
    to_move.reverse()
    for item in to_move:
        stacks[dest].append(item)

def part1():
    stacks = parse()
    res = ""
    for instruction in instructions:
        move(stacks, instruction)
    for stack in stacks:
        if len(stack) > 0:
            res += stack[-1]
    return res

def part2():
    stacks = parse()
    res = ""
    for instruction in instructions:
        move2(stacks, instruction)
    for stack in stacks:
        if len(stack) > 0:
            res += stack[-1]
    return res


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(5, ans1, ans2, time1, time2)
