from util.files import *
from util.runner import *
import time

TESTING = False

lines = GetLines(25, TESTING)

class SnafuNumber:
    def __init__(self, val = None):
        self.val = val or "0"

    def __add__(self, other: "SnafuNumber") -> "SnafuNumber":
        dv = int(self.base_5, 5) + int(other.base_5, 5)
        rv = ""
        while dv:
            rv += str(dv % 5)
            dv = dv // 5
        return SnafuNumber.from_base_5(rv[::-1])

    @property
    def base_5(self) -> str:
        result = ""
        carry = 0
        for v in map(self.sd_to_dd, self.val[::-1]):
            v -= carry
            carry = 1 if v < 0 else 0
            result += str(v + (5 if v < 0 else 0))
        return "".join((map(str, result[::-1]))).lstrip("0") or "0"

    @classmethod
    def from_base_5(cls, value: str) -> "SnafuNumber":
        sn = []
        carry = 0
        for v in [int(i) for i in reversed(value)]:
            nv = v + carry
            carry = 1 if nv > 2 else 0
            sn.append(cls.dd_to_sd(nv - (5 if nv > 2 else 0)))
        sn.append(str(carry))
        return SnafuNumber("".join(map(str, sn[::-1])).lstrip("0"))

    @classmethod
    def sd_to_dd(cls, v: str) -> int:
        return -1 if v == "-" else -2 if v == "=" else int(v)

    @classmethod
    def dd_to_sd(cls, v: int) -> str:
        return "-" if v == -1 else "=" if v == -2 else str(v)

def parse(lines):
    _ = lines
    return

def part1():
    return sum(map(SnafuNumber, lines), SnafuNumber()).val

def part2():
    return "NONE"


start1 = time.perf_counter()
ans1 = part1()
time1 = time.perf_counter() - start1

start2 = time.perf_counter()
ans2 = part2()
time2 = time.perf_counter() - start2

RunDay(25, ans1, ans2, time1, time2)
