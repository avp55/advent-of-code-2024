import os
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop
import sys

sys.setrecursionlimit(150000)


def read_input() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, "input.txt")
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def convert_line_to_nums(line):
    return [int(x) for x in line.split()]


def read_input_converted(input):
    return [convert_line_to_nums(line) for line in input]


def matrix_to_heights(matrix):
    results = [0] * len(matrix[0])
    for j in range(len(matrix[0])):
        count = 0
        for i in range(len(matrix)):
            if matrix[i][j] == "#":
                count += 1
        results[j] = count
    return results


def part1():
    locks = []
    keys = []
    input = read_input()
    curr = []
    max_height = 0
    for line in input:
        if not line:
            if "#" in curr[0]:
                max_height = len(curr)
                locks.append(matrix_to_heights(curr))
            else:
                keys.append(matrix_to_heights(curr))
            curr = []
        else:
            curr.append(line)
    if curr:
        if "#" in curr[0]:
            locks.append(matrix_to_heights(curr))
        else:
            keys.append(matrix_to_heights(curr))
    total = 0
    for l in locks:
        for k in keys:
            does_fit = True
            for i in range(len(k)):
                if l[i] + k[i] > max_height:
                    does_fit = False
                    break
            if does_fit:
                total += 1
    print(total)


def part2():
    read_input()


part1()
