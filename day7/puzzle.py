import os
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop
import sys
sys.setrecursionlimit(150000)


def read_input() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'input1.txt')
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def convert_line_to_nums(line):
    return [int(x) for x in line.split()]


def read_input_converted(input):
    return [convert_line_to_nums(line) for line in input]


def part1():
    lines = read_input()
    sm = 0
    for line in lines:
        line = line.split()
        total = int(line[0][0:-1])
        numbers = [int(x) for x in line[1:]]
        if can_produce(numbers, total):
            sm += total
    print(sm)


def can_produce(input, target):
    if len(input) == 1:
        return input[0] == target
    opt1 = input[0] + input[1]
    opt2 = input[0] * input[1]
    next_a = input[2:]
    return can_produce([opt1, *next_a], target) or can_produce([opt2, *next_a], target)


def can_produce_part2(input, target):
    if len(input) == 1:
        return input[0] == target
    opt1 = input[0] + input[1]
    opt2 = input[0] * input[1]
    opt3 = int(str(input[0])+str(input[1]))
    next_a = input[2:]
    return can_produce_part2([opt1, *next_a], target) or can_produce_part2([opt2, *next_a], target) or can_produce_part2([opt3, *next_a], target)


def part2():
    lines = read_input()
    sm = 0
    for line in lines:
        line = line.split()
        total = int(line[0][0:-1])
        numbers = [int(x) for x in line[1:]]
        if can_produce_part2(numbers, total):
            sm += total
    print(sm)


part1()
part2()
