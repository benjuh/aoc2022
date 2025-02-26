from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(3, TESTING)

rucksacks = [[]]
groups = []
def parse(lines):
    rucksacks.clear()
    for line in lines:
        middle = len(line) // 2
        left = line[:middle]
        right = line[middle:]
        rucksack = [left, right]
        rucksacks.append(rucksack)
    
    i = 0
    for _ in range(len(lines)//3):
        group = [lines[i], lines[i+1], lines[i+2]]
        groups.append(group)
        i += 3

    build_priority_values()
    return

value_of = {}
def build_priority_values():
    i = 1
    for char in 'abcdefghijklmnopqrstuvwxyz':
        value_of[char] = i
        i += 1
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        value_of[char] = i
        i += 1
    return

def part1():
    parse(lines)
    total = 0

    for rucksack in rucksacks:
        scored_chars = set()
        char_map_left = set()
        for char in rucksack[0]:
            char_map_left.add(char)
        for char in rucksack[1]:
            if char in char_map_left and char not in scored_chars:
                total += value_of[char]
                scored_chars.add(char)
    return total

def part2():
    total = 0
    for group in groups:
        char_map_1 = set()
        char_map_2 = set()
        char_map_3 = set()
        i = 0
        for rucksack in group:
            if i == 0:
                for char in rucksack:
                    char_map_1.add(char)
            if i == 1:
                for char in rucksack:
                    char_map_2.add(char)
            if i == 2:
                for char in rucksack:
                    char_map_3.add(char)
            i+=1
        for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if char in char_map_1 and char in char_map_2 and char in char_map_3:
                total += value_of[char]

    return total


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(3, ans1, ans2, time1, time2)
