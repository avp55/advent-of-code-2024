from copy import deepcopy
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
    input = read_input()
    input = [[x for x in y] for y in input]
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] in ['^', '>', '<', 'v']:
                res = dfs(i, j, input[i][j], input)
                print(res)
                return


mp = {
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0),
    '^': (-1, 0)
}

rot = {
    '>': 'v',
    '<': '^',
    'v': '<',
    '^': '>'
}


def dfs(x, y, curr, grid):
    mx, my = mp[curr]
    nx, ny = x+mx, y+my
    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
        grid[x][y] = 'X'
        return 1
    if grid[nx][ny] == '.' or grid[nx][ny] == 'X':
        grid[x][y] = 'X'
        val = 1 if grid[nx][ny] == '.' else 0
        return val + dfs(nx, ny, curr, grid)
    next_curr = rot[curr]
    return dfs(x, y, next_curr, grid)


def find_start(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] in ['^', '>', '<', 'v']:
                return (i, j)
    return None


def dfs2(x, y, curr, grid, visited):
    if (x, y, curr) in visited:
        return True
    visited.add((x, y, curr))
    mx, my = mp[curr]
    nx, ny = x+mx, y+my
    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
        return False
    if grid[nx][ny] != '#':
        return dfs2(nx, ny, curr, grid, visited)
    next_curr = rot[curr]
    return dfs2(x, y, next_curr, grid, visited)


def part2():
    input = read_input()
    input = [[x for x in y] for y in input]
    start = find_start(input)
    sx, sy = start
    total = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if ((i, j) == start) or input[i][j] == '#':
                continue
            input[i][j] = '#'
            if dfs2(sx, sy, input[sx][sy], input, set()):
                total += 1
            input[i][j] = '.'
    print(total)


part1()
part2()
