from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(2, TESTING)
 
value_of = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

rock_outcomes = {
    'A': 3,
    'B': 0,
    'C': 6,
}

paper_outcomes = {
    'A': 6,
    'B': 3,
    'C': 0
}

scissors_outcomes = {
    'A': 0,
    'B': 6,
    'C': 3,
}

necessary_move_against_rock = ['Z',0,0,'X',0,0,'Y']
necessary_move_against_paper = ['X',0,0,'Y',0,0,'Z']
necessary_move_against_scissors = ['Y',0,0,'Z',0,0,'X']

matches = []
def parse(lines):
    matches.clear()
    for line in lines:
        match = []
        played = line.split(" ")
        for i in range(len(played)):
            match.append(played[i])
        matches.append(match)
    return

def part1():
    parse(lines)
    total = 0
    for match in matches:
        opponent = match[0]
        player = match[1]

        if player == 'X':
            total += value_of[player] + rock_outcomes[opponent]
        if player == 'Y':
            total += value_of[player] + paper_outcomes[opponent]
        if player == 'Z':
            total += value_of[player] + scissors_outcomes[opponent]
    return total

def part2():
    parse(lines)
    total = 0
    for match in matches:
        opponent = match[0]
        condition = match[1]
        condition_to_index = {
            'X': 0,
            'Y': 3,
            'Z': 6
        }
        index = condition_to_index[condition]
        if opponent == 'A':
            total += value_of[necessary_move_against_rock[index]] + index
        if opponent == 'B':
            total += value_of[necessary_move_against_paper[index]] + index
        if opponent == 'C':
            total += value_of[necessary_move_against_scissors[index]] + index

    return total


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(2, ans1, ans2, time1, time2)
