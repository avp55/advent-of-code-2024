import os
from collections import defaultdict, Counter, deque
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


def bfs(grid, ex, ey):
    q = deque([(0, 0)])
    visited = set()
    ex, ey = len(grid) - 1, len(grid) - 1
    level = 0
    opts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == (ex, ey):
                return level
            if grid[x][y] == "#":
                continue
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for ox, oy in opts:
                nx, ny = x + ox, y + oy
                if (
                    nx < 0
                    or ny < 0
                    or nx >= len(grid)
                    or ny >= len(grid[0])
                    or grid[nx][ny] == "#"
                ):
                    continue
                q.append((nx, ny))
        level += 1
    return -1


def part1():
    # at 0,0, need to reach 6,6 or 70,70
    # coordinates from 0-6 or 0-70
    # X Y but reversed x=j y=i
    grid_size = 71
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    input = read_input()
    for i, line in enumerate(input):
        if i >= 1024:
            break
        line = line.split(",")
        x, y = line
        x, y = int(x), int(y)
        grid[y][x] = "#"
    print(bfs(grid, len(grid) - 1, len(grid) - 1))
    # for k in grid:
    #    print("".join(k))


def part2():
    # at 0,0, need to reach 6,6 or 70,70
    # coordinates from 0-6 or 0-70
    # X Y but reversed x=j y=i
    grid_size = 71
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    input = read_input()
    # Could use binary search to speed this up, still fast enough
    for i, line in enumerate(input):
        line = line.split(",")
        x, y = line
        x, y = int(x), int(y)
        grid[y][x] = "#"
        if i < 1024:
            continue
        if bfs(grid, len(grid) - 1, len(grid) - 1) == -1:
            print("Unpassable", i, line)
            return


part2()
