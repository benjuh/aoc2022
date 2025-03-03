from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(23, TESTING)

from collections import defaultdict
import operator

start1 = time.perf_counter()
dirs = {"N": [(-1, 0), (-1, 1), (-1, -1)], "S": [(1, 0), (1, 1,), (1, -1)],
        "W": [(0, -1), (-1, -1), (1, -1)], "E": [(0, 1), (-1, 1), (1, 1)]}
dirs_all = set(dirs["N"] + dirs["S"] + dirs["W"] + dirs["E"])
queue = ["N", "S", "W", "E"]
empty = None
def add(t1, t2):
    return tuple(map(operator.add, t1, t2))

pos_elves = [(r, c) for c in range(len(lines[0])) for r in range(len(lines)) if lines[r][c] == "#"]
r = 0
while True:
    r += 1
    pos_elves_speedup = set(pos_elves)
    moves = defaultdict(list)
    for idx, pos in enumerate(pos_elves):
        if not any(add(pos, d) in pos_elves_speedup for d in dirs_all):
            continue

        for nt in queue:
            if not any(add(pos, d) in pos_elves_speedup for d in dirs[nt]):
                moves[add(pos, dirs[nt][0])].append(idx)
                break

    queue.append(queue.pop(0))

    some_move = False
    for pos, idxs in moves.items():
        if len(idxs) == 1:
            pos_elves[idxs[0]] = pos
            some_move = True

    if r == 10:
        mir, mar = min(t[0] for t in pos_elves), max(t[0] for t in pos_elves)
        mic, mac = min(t[1] for t in pos_elves), max(t[1] for t in pos_elves)
        empty = (mar - mir + 1) * (mac - mic + 1) - len(pos_elves)

    if not some_move:
        break

time1 = time.perf_counter() - start1
ans1 = empty
ans2 = r

RunDay(23, ans1, ans2, time1, time1)
