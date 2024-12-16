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


def dfs(grid, x, y, item, collect, visited):
    if grid[x][y] != item or (x, y) in visited:
        return
    collect.append((x, y))
    visited.add((x, y))
    opts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for ox, oy in opts:
        nx, ny = x+ox, y+oy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
            continue
        dfs(grid, nx, ny, item, collect, visited)


def count_perimeter(grid, x, y):
    # up, down, left, right
    opts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    total = 0
    for ox, oy in opts:
        nx, ny = x+ox, y+oy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
            total += 1
        elif grid[nx][ny] != grid[x][y]:
            total += 1
    return total


def part1():
    input = read_input()
    visited = set()
    total = 0
    for i in range(len(input)):
        collect_region = []
        for j in range(len(input[0])):
            collect_region = []
            dfs(input, i, j, input[i][j], collect_region, visited)
            if not collect_region:
                continue
            area = len(collect_region)
            perimeter = 0
            for x, y in collect_region:
                perimeter += count_perimeter(input, x, y)
            total += (perimeter*area)
    print(total)
    # area is the number inside each region
    # perimeter is the sides - 4x per letter unless touching one of the same
    # more if touching a different letter potentially
    # for each region, find perimeter*area


def can_fence(grid, nx, ny, x, y):
    return (nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0])) or grid[nx][ny] != grid[x][y]


def count_perimeter_2(grid, x, y, visited):
    # up, down, left, right
    total = 0
    mp = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
    for k, v in mp.items():
        ox, oy = v
        if (x, y, k) in visited:
            continue
        visited.add((x, y, k))
        nx, ny = x+ox, y+oy
        fenceable = can_fence(grid, nx, ny, x, y)
        if not fenceable:
            continue
        if k == 'UP' or k == 'DOWN':
            left = y-1
            while left > -1 and grid[x][left] == grid[x][y]:
                if not can_fence(grid, nx, left, x, y):
                    break
                if (x, left, k) in visited:
                    break
                visited.add((x, left, k))
                left -= 1
            right = y+1
            while right < len(grid[0]) and grid[x][right] == grid[x][y]:
                if not can_fence(grid, nx, right, x, y):
                    break
                if (x, right, k) in visited:
                    break
                visited.add((x, right, k))
                right += 1
        else:
            up = x-1
            while up > -1 and grid[up][y] == grid[x][y]:
                if not can_fence(grid, up, ny, x, y):
                    break
                if (up, y, k) in visited:
                    break
                visited.add((up, y, k))
                up -= 1
            down = x+1
            while down < len(grid) and grid[down][y] == grid[x][y]:
                if not can_fence(grid, down, ny, x, y):
                    break
                if (down, y, k) in visited:
                    break
                visited.add((down, y, k))
                down += 1
        total += 1
    return total


def part2():
    input = read_input()
    visited = set()
    total = 0
    visited_p = set()
    for i in range(len(input)):
        collect_region = []
        for j in range(len(input[0])):
            collect_region = []
            dfs(input, i, j, input[i][j], collect_region, visited)
            if not collect_region:
                continue
            area = len(collect_region)
            perimeter = 0
            for x, y in collect_region:
                pem = count_perimeter_2(input, x, y, visited_p)
                perimeter += pem
            total += (perimeter*area)
    print(total)


part1()
part2()
