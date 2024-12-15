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


def in_bounds(x, y, grid):
    if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]):
        return True
    return False


def part1():
    input = read_input()
    spots = defaultdict(list)
    for i in range(len(input)):
        for j in range(len(input[0])):
            item = input[i][j]
            if item == '.':
                continue
            spots[item].append((i, j))
    total = set()
    for v in spots.values():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                ix, iy = v[i]
                jx, jy = v[j]
                xdiff = jx-ix
                ydiff = jy-iy

                ixn, iyn = ix - xdiff, iy - ydiff
                jxn, jyn = jx + xdiff, jy + ydiff
                if in_bounds(ixn, iyn, input):
                    total.add((ixn, iyn))
                if in_bounds(jxn, jyn, input):
                    total.add((jxn, jyn))
    print(len(total))


part1()


def part2():
    input = read_input()
    spots = defaultdict(list)
    for i in range(len(input)):
        for j in range(len(input[0])):
            item = input[i][j]
            if item == '.':
                continue
            spots[item].append((i, j))
    total = set()
    for v in spots.values():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                ix, iy = v[i]
                jx, jy = v[j]
                total.add((ix, iy))
                total.add((jx, jy))
                xdiff = jx-ix
                ydiff = jy-iy
                while True:
                    ix -= xdiff
                    iy -= ydiff
                    if in_bounds(ix, iy, input):
                        total.add((ix, iy))
                    else:
                        break
                while True:
                    jx += xdiff
                    jy += ydiff
                    if in_bounds(jx, jy, input):
                        total.add((jx, jy))
                    else:
                        break

    print(len(total))


part2()
