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


def shortest_path(x, y, input):
    hp = [(0, x, y)]
    opts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    while hp:
        score, x, y = heappop(hp)
        if input[x][y] == "E":
            return score
        if input[x][y] == "#":
            continue
        key = (x, y)
        score += 1
        if key in visited:
            continue
        visited.add(key)
        for ox, oy in opts:
            nx, ny = x + ox, y + oy
            if nx < 0 or ny < 0 or nx >= len(input) or ny >= len(input):
                continue
            heappush(hp, (score, nx, ny))


def compute_dist(sx, sy, ex, ey, input):
    dist = {}
    q = deque([(sx, sy, 0)])
    opts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        x, y, score = q.popleft()
        if (x, y) == (ex, ey):
            if (x, y) not in dist:
                dist[(x, y)] = score
            continue
        if (x, y) in dist:
            continue
        dist[(x, y)] = score
        for ox, oy in opts:
            nx, ny = ox + x, oy + y
            if (
                nx < 0
                or ny < 0
                or nx >= len(input)
                or ny >= len(input[0])
                or input[nx][ny] == "#"
            ):
                continue
            q.append((nx, ny, score + 1))
    return dist


# Veeeery slow but it works, 10k dijkstra iterations
def part1():
    input = read_input()
    input = [[x for x in y] for y in input]
    x, y = None, None
    walls = set()
    opts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "S":
                x, y = i, j
            elif input[i][j] == "#":
                for ox, oy in opts:
                    nx, ny = ox + i, oy + j
                    if (
                        nx > -1
                        and ny > -1
                        and nx < len(input)
                        and ny < len(input[0])
                        and input[nx][ny] != "#"
                    ):
                        walls.add((i, j))
    normal_time = shortest_path(x, y, input)
    at_least = normal_time - 100
    total = 0
    for i, j in walls:
        input[i][j] = "."
        res = shortest_path(x, y, input)
        if res <= at_least:
            total += 1
            print(res)
        input[i][j] = "#"
    print(total)


def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def generate_all_points(diff, sx, sy):
    pdiffs = set()
    for i in range(-diff, diff + 1, 1):
        for j in range(-diff, diff + 1, 1):
            if manhattan_distance(sx, sx + i, sy, sy + j) < diff + 1:
                pdiffs.add((i, j))
    return pdiffs


# More intelligent
def part2():
    # for every point, compute how far it is from the start
    input = read_input()
    input = [[x for x in y] for y in input]
    x, y = None, None
    ex, ey = None, None
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "S":
                x, y = i, j
                break
            elif input[i][j] == "E":
                ex, ey = i, j
        if x and y and ex and ey:
            break
    distances = compute_dist(x, y, ex, ey, input)
    minimum_save = 100
    diff = 20
    total = 0
    for k, v in distances.items():
        x, y = k
        for gx, gy in generate_all_points(diff, x, y):
            nx, ny = x + gx, y + gy
            if nx < 0 or ny < 0 or nx >= len(input) or ny >= len(input):
                continue
            if (nx, ny) not in distances:
                continue
            calc = v - (distances[(nx, ny)] + manhattan_distance(nx, x, ny, y))
            if calc >= minimum_save:
                total += 1
    print(total)


part2()
