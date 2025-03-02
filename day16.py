from util.files import *
from util.runner import *
import time
import itertools
import re

def parse():
    with open("data/day16.txt") as f:
        return [re.findall('[A-Z]+|\\d+', line[1:]) for line in f.readlines()]

def part1():
    puzzle = parse()
    graph = {valve:leads for valve, _, *leads in puzzle}
    flows = {valve: int(flow) for valve, flow, *_ in puzzle if flow != '0'}
    indicies = {valve: 1 << i for i, valve in enumerate(flows)}
    distances = {(v,l): 1 if l in graph[v] else 1000 for l in graph for v in graph}

    def visit(valve, minutes, bitmask, pressure, answer):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        for valve2, flow in flows.items():
            remaining_minutes = minutes - distances[valve, valve2] - 1
            if indicies[valve2] & bitmask or remaining_minutes <= 0: continue
            visit(valve2, remaining_minutes, bitmask|indicies[valve2], pressure + flow * remaining_minutes, answer)
        return answer
    # floyd-warshall = Distance for any possible pair of valves
    for k, i, j in itertools.permutations(graph, 3):
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    return max(visit('AA', 30, 0, 0, {}).values())

def part2():
    puzzle = parse()
    graph = {valve:leads for valve, _, *leads in puzzle}
    flows = {valve: int(flow) for valve, flow, *_ in puzzle if flow != '0'}
    indicies = {valve: 1 << i for i, valve in enumerate(flows)}
    distances = {(v,l): 1 if l in graph[v] else 1000 for l in graph for v in graph}

    def visit(valve, minutes, bitmask, pressure, answer):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        for valve2, flow in flows.items():
            remaining_minutes = minutes - distances[valve, valve2] - 1
            if indicies[valve2] & bitmask or remaining_minutes <= 0: continue
            visit(valve2, remaining_minutes, bitmask|indicies[valve2], pressure + flow * remaining_minutes, answer)
        return answer
    # floyd-warshall = Distance for any possible pair of valves
    for k, i, j in itertools.permutations(graph, 3):
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    visited2  = visit('AA', 26, 0, 0, {})
    return max(v1+v2 for bitm1, v1 in visited2.items()
        for bitm2, v2 in visited2.items() if not bitm1 & bitm2)


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(16, ans1, ans2, time1, time2)
