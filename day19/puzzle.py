import os
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop
import sys
sys.setrecursionlimit(150000)


def read_input() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'input.txt')
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def convert_line_to_nums(line):
    return [int(x) for x in line.split()]


def read_input_converted(input):
    return [convert_line_to_nums(line) for line in input]


def can_build(pos, input, available, memo):
    key = (pos, input)
    if key in memo:
        return memo[key]
    if not input:
        return True
    if pos > len(input):
        return False
    current = input[:pos]
    option1 = False
    if current in available:
        option1 = can_build(0, input[pos:], available, memo)
    memo[key] = can_build(pos+1, input, available, memo) or option1
    return memo[key]


def part1():
    input = read_input()
    blocks = set()
    create = []
    total = 0
    for i in range(len(input)):
        if i == 0:
            for x in input[i].split(', '):
                blocks.add(x)
        elif input[i]:
            create.append(input[i])
    for c in create:
        if can_build(0, c, blocks, {}):
            total += 1
    print(total)


def can_build2(pos, input, available, memo):
    key = (pos, input)
    if key in memo:
        return memo[key]
    if not input:
        return 1
    if pos > len(input):
        return 0
    current = input[:pos]
    option1 = 0
    if current in available:
        option1 = can_build2(0, input[pos:], available, memo)
    memo[key] = can_build2(pos+1, input, available, memo) + option1
    return memo[key]


def part2():
    input = read_input()
    blocks = set()
    create = []
    total = 0
    for i in range(len(input)):
        if i == 0:
            for x in input[i].split(', '):
                blocks.add(x)
        elif input[i]:
            create.append(input[i])
    for c in create:
        total += can_build2(0, c, blocks, {})
    print(total)


part1()
part2()
