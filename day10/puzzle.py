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


def dfs(input, x, y, seen):
    if input[x][y] == 9:
        if (x, y) in seen:
            return 0
        seen.add((x, y))
        return 1
    opts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total = 0
    for ox, oy in opts:
        nx, ny = x+ox, y+oy
        if nx < 0 or nx >= len(input) or ny < 0 or ny >= len(input[0]):
            continue
        if input[nx][ny] - input[x][y] == 1:
            total += dfs(input, nx, ny, seen)
    return total


def dfs2(input, x, y, seen):
    if input[x][y] == 9:
        return 1
    opts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total = 0
    for ox, oy in opts:
        nx, ny = x+ox, y+oy
        if nx < 0 or nx >= len(input) or ny < 0 or ny >= len(input[0]):
            continue
        if input[nx][ny] - input[x][y] == 1:
            total += dfs2(input, nx, ny, seen)
    return total


def part1():
    # path from 0-9 step of 1, 4 dirs only
    input = read_input()
    input = [[int(x) for x in y] for y in input]
    # print(input)
    total = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                total += (dfs(input, i, j, set()))
    print(total)


def part2():
    # path from 0-9 step of 1, 4 dirs only
    input = read_input()
    input = [[int(x) for x in y] for y in input]
    # print(input)
    total = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                total += (dfs2(input, i, j, set()))
    print(total)


part1()
part2()
