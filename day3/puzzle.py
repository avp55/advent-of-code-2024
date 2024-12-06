import os
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop
import re


def read_input() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'part1.txt')
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def convert_line_to_nums(line):
    return [int(x) for x in line.split()]


def read_input_conv(input):
    return [convert_line_to_nums(line) for line in input]


pattern = r'mul\((\d+)\s*,\s*(\d+)\)'


def part1():
    input = read_input()
    print(len(input))
    total = 0
    for line in input:

        matches = re.findall(pattern, line)
        for fr, sc in matches:
            total += (int(fr) * int(sc))
    print(total)


def part2():
    input = read_input()
    total = 0
    can_continue = True
    line = ''.join(input)
    for i in range(len(line)):
        s = line[i:]
        if s.startswith("don't()"):
            can_continue = False
        elif s.startswith('do()'):
            can_continue = True
        elif can_continue:
            match = re.match(pattern, s)
            if match:
                num1, num2 = match.group(1), match.group(2)
                total += (int(num1) * int(num2))
    print(total)


part1()
part2()
