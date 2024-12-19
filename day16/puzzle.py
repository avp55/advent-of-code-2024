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


def part1():
    input = read_input()
    # start S facing east, need to reach E - 1 point per move
    # can rotate +90 or -90 incresing score by 1000
    x, y = None, None
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'S':
                x, y = i, j
                break
        if x and y:
            break
    hp = [(0, x, y, 0, 1)]
    rotation = {
        'counter': {
            (0, 1): (-1, 0),
            (0, -1): (1, 0),
            (1, 0): (0, 1),
            (-1, 0): (0, -1),
        },
        'clock': {
            (0, 1): (1, 0),
            (0, -1): (-1, 0),
            (1, 0): (0, -1),
            (-1, 0): (0, 1),
        }
    }
    visited = set()
    while hp:
        score, x, y, dx, dy = heappop(hp)
        if input[x][y] == '#':
            continue
        if input[x][y] == 'E':
            return score

        key = (x, y, dx, dy)
        if key in visited:
            continue
        visited.add(key)

        heappush(hp, (score+1, x+dx, y+dy, dx, dy))

        dxcc, dycc = rotation['counter'][(dx, dy)]
        dxcl, dycl = rotation['clock'][(dx, dy)]

        heappush(hp, (score+1001, x+dxcc, y+dycc, dxcc, dycc))
        heappush(hp, (score+1001, x+dxcl, y+dycl, dxcl, dycl))

    return -1


def part2():
    input = read_input()
    input = [[x for x in y] for y in input]
    # start S facing east, need to reach E - 1 point per move
    # can rotate +90 or -90 incresing score by 1000
    x, y = None, None
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'S':
                x, y = i, j
                break
        if x and y:
            break
    hp = [(0, x, y, 0, 1, [])]
    rotation = {
        'counter': {
            (0, 1): (-1, 0),
            (0, -1): (1, 0),
            (1, 0): (0, 1),
            (-1, 0): (0, -1),
        },
        'clock': {
            (0, 1): (1, 0),
            (0, -1): (-1, 0),
            (1, 0): (0, -1),
            (-1, 0): (0, 1),
        }
    }
    visited = {}
    min_score = float('inf')
    points = []
    while hp:
        score, x, y, dx, dy, path = heappop(hp)
        if input[x][y] == '#':
            continue
        if input[x][y] == 'E' and score <= min_score:
            min_score = score
            points += path
        elif input[x][y] == 'E':
            continue
        key = (x, y, dx, dy)
        if key in visited and visited[key] < score:
            continue
        visited[key] = score
        path.append((x, y))

        heappush(hp, (score+1, x+dx, y+dy, dx, dy, path[:]))

        dxcc, dycc = rotation['counter'][(dx, dy)]
        dxcl, dycl = rotation['clock'][(dx, dy)]

        heappush(hp, (score+1001, x+dxcc, y+dycc, dxcc, dycc, path[:]))
        heappush(hp, (score+1001, x+dxcl, y+dycl, dxcl, dycl, path[:]))
    print(len(set(points))+1)


print(part1())
part2()
