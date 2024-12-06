import os
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop


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


def read_input_converted(input):
    return [convert_line_to_nums(line) for line in input]


def part1():
    input = read_input()
    input = [[y for y in x] for x in input]
    total = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0),
                          (-1, -1), (1, 1), (-1, 1), (1, -1)]
            for dir in directions:
                total += dfs(i, j, 0, input, 'XMAS', dir)

    print(total)


def dfs(x, y, n, grid, search, directions):
    if grid[x][y] != search[n]:
        return 0
    if n+1 >= len(search):
        return 1
    total = 0
    dx, dy = directions
    nx, ny = dx+x, dy+y
    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
        return 0
    total += dfs(nx, ny, n+1, grid, search, directions)
    return total


def all_inbounds(opts, input, x, y):
    for ox, oy in opts:
        nx, ny = ox+x, oy+y
        if nx < 0 or ny < 0 or nx >= len(input) or ny >= len(input[0]):
            return False
    return True


def at_least_one_variant_matching(variants, x, y, opts, input):
    for var in variants:
        all_fit = True
        for ox, oy in opts:
            nx, ny = x+ox, y+oy
            if input[nx][ny] != var[(ox, oy)]:
                all_fit = False
                break
        if all_fit:
            return True
    return False


def part2():
    input = read_input()
    input = [[y for y in x] for x in input]
    total = 0
    up_left = (-1, -1)
    up_right = (-1, 1)
    down_left = (1, -1)
    down_right = (1, 1)
    variants = [
        {
            up_left: 'M',
            up_right: 'S',
            down_left: 'M',
            down_right: 'S'
        },
        {
            up_left: 'S',
            up_right: 'M',
            down_left: 'S',
            down_right: 'M'
        },
        {
            up_left: 'S',
            up_right: 'S',
            down_left: 'M',
            down_right: 'M'
        },
        {
            up_left: 'M',
            up_right: 'M',
            down_left: 'S',
            down_right: 'S'
        }
    ]
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'A':
                opts = [up_left, up_right, down_left, down_right]
                # Check to see if cross can be made
                if not all_inbounds(opts, input, i, j):
                    continue
                # Of all the cross permutations, is at least one matching
                if at_least_one_variant_matching(variants, i, j, opts, input):
                    total += 1
    print(total)


part1()
part2()
