from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(7, TESTING)

def parse(lines):
    _ = lines
    return

def tree():
    pwd = ""
    directories = { "/root" : 0 }
    for line in lines:
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == "..":
                    pwd = pwd[:pwd.rindex("/")]
                elif line[2] == "/":
                    pwd = "/root"
                else:
                    pwd += "/" + line[2]
                    directories[pwd] = 0
        else:
            if line[0] != "dir":
                temp = pwd
                while temp != "":
                    directories[temp] += int(line[0])
                    temp = temp[:temp.rindex("/")]
    return directories




def part1():
    directories = tree()
    total = 0
    for _, size in directories.items():
        if size < 100000:
            total += size
    return total

def part2():
    directories = tree()
    at_least = 30000000
    at_most = 70000000
    required = directories["/root"] - (at_most - at_least)
    smallest_deletable = directories["/root"]
    for _, directory in directories.items():
        if required < directory < smallest_deletable:
            smallest_deletable = directory
    return smallest_deletable


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(7, ans1, ans2, time1, time2)
