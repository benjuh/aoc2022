from util.files import *
from util.runner import *
import time
from operator import mul, add, sub, truediv
from collections import namedtuple

TESTING = False

lines = GetLinesNoStrip(21, TESTING)
Monkey = namedtuple("Monkey", ("name", "number", "operand1", "operator", "operand2"))
monkeys:dict[str, Monkey] = {}

def parse(lines):
    for line in lines:
        mk_name, mk_value = line.split(":")
        if (mk_value.count(" ") == 1):
            monkey = Monkey(mk_name, int(mk_value), None, None, None)
        else:
            mk_val1, mk_opt, mk_val2 = mk_value.strip().split()
            match mk_opt:
                case "+":
                    mk_opt = add
                case "-":
                    mk_opt = sub
                case "*":
                    mk_opt = mul
                case "/":
                    mk_opt = truediv
            assert callable(mk_opt)
            monkey = Monkey(mk_name, None, mk_val1, mk_opt, mk_val2)
        
        monkeys[mk_name] = monkey
    return

def get_monkey_number(monkey_name):
    monkey = monkeys[monkey_name]
    if monkey.number is not None:
        return monkey.number
    else:
        return monkey.operator(
            get_monkey_number(monkey.operand1),
            get_monkey_number(monkey.operand2)
        )


def part1():
    parse(lines)
    return round(get_monkey_number("root"))

def part2():
    parse(lines)
    previous_number = monkeys["humn"].number
    monkeys["root"] = Monkey("root", None, monkeys["root"].operand1, sub, monkeys["root"].operand2)
    target = get_monkey_number("root")
    previous_error = abs(target)
    my_number = 0
    monkeys["humn"] = Monkey("humn", my_number, None, None, None)
    target = get_monkey_number("root")
    my_error = abs(target)
    rate = 0.1

    while (my_error > 0.1):
        try:
            gradient = (my_number - previous_number) // (my_error - previous_error)
        except ZeroDivisionError:
            gradient = 1 if my_error < previous_error else -1
        previous_number = my_number
        previous_error = my_error

        my_number -= rate * my_error * gradient
        monkeys["humn"] = Monkey("humn", my_number, None, None, None)
        
        target = get_monkey_number("root")
        my_error = abs(target)
    return round(my_number)


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(21, ans1, ans2, time1, time2)
