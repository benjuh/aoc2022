from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(11, TESTING)

monkeys = []
operations = []
tests = []

def parse(): 
    i = 0
    mod = 1
    monkeys.clear()
    operations.clear()
    tests.clear()
    while i < len(lines):
        items_line = i+1
        operation_line = i+2
        test_line = i+3
        if_line = i+4
        else_line = i+5

        items = lines[items_line].split(": ")[1].split(", ")
        items = [int(x) for x in items]
        monkeys.append(items)

        ops = lines[operation_line].split("Operation: new = old ")[1].split(" ")
        operations.append((ops[0], ops[1]))

        test = int(lines[test_line].split("Test: divisible by ")[1])
        mod *= test
        do_if = int(lines[if_line][-1])
        do_else = int(lines[else_line][-1])
        tests.append((test, do_if, do_else))
        i += 7

    return mod

def part1():
    _ = parse()
    rounds = 20
    inspections = [0] * len(monkeys)
    for _ in range(rounds):
        for id, items in enumerate(monkeys):
            while len(items) > 0:
                item = items.pop(0)
                op, operand = operations[id]
                new = item
                if operand == 'old':
                    operand = item
                else:
                    operand = int(operand)
                if op == '*':
                    new *= operand
                elif op == '+':
                    new += operand
                new //= 3
                divisor, send_to_if, send_to_else = tests[id]
                if new % divisor == 0:
                    monkeys[send_to_if].append(new)
                else:
                    monkeys[send_to_else].append(new)
                inspections[id] += 1
    
    inspections.sort()
    return inspections[-2] * inspections[-1]

def part2():
    mod = parse()
    rounds = 10000
    inspections = [0] * len(monkeys)
    for i in range(rounds):
        for id, items in enumerate(monkeys):
            while len(items) > 0:
                item = items.pop(0)
                op, operand = operations[id]
                new = item
                if operand == 'old':
                    operand = item
                else:
                    operand = int(operand)
                if op == '*':
                    new *= operand
                elif op == '+':
                    new += operand
                divisor, send_to_if, send_to_else = tests[id]
                new %= mod
                if new % divisor == 0:
                    monkeys[send_to_if].append(new)
                else:
                    monkeys[send_to_else].append(new)
                inspections[id] += 1
    
    inspections.sort()
    return inspections[-2] * inspections[-1]


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(11, ans1, ans2, time1, time2)
