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
    map = []
    instructions = ''
    read_map = True
    mp = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }
    for i in range(len(input)):
        if not input[i]:
            read_map = False
            continue
        if read_map:
            map.append([x for x in input[i]])
        else:
            instructions += input[i]
    x, y = None, None
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                x, y = i, j
                break
        if x and y:
            break
    for inst in instructions:
        dx, dy = mp[inst]
        nx, ny = dx+x, dy+y
        if nx < 0 or ny < 0 or nx >= len(map) or ny >= len(map[0]) or map[nx][ny] == '#':
            continue
        if map[nx][ny] == '.':
            map[x][y] = '.'
            x, y = nx, ny
            map[nx][ny] = '@'
            continue
        if inst == '^':
            start = x
            obstacle_count = 0
            while start > -1:
                if map[start][y] == 'O':
                    obstacle_count += 1
                elif map[start][y] == '#':
                    break
                elif map[start][y] == '.':
                    while obstacle_count > 0:
                        map[start][y] = 'O'
                        start += 1
                        obstacle_count -= 1
                    map[start][y] = '@'
                    map[x][y] = '.'
                    x, y = start, y
                    break
                start -= 1
        elif inst == 'v':
            start = x
            obstacle_count = 0
            while start < len(map):
                if map[start][y] == 'O':
                    obstacle_count += 1
                elif map[start][y] == '#':
                    break
                elif map[start][y] == '.':
                    while obstacle_count > 0:
                        map[start][y] = 'O'
                        start -= 1
                        obstacle_count -= 1
                    map[start][y] = '@'
                    map[x][y] = '.'
                    x, y = start, y
                    break
                start += 1
        elif inst == '<':
            start = y
            obstacle_count = 0
            while y > -1:
                if map[x][start] == 'O':
                    obstacle_count += 1
                elif map[x][start] == '#':
                    break
                elif map[x][start] == '.':
                    while obstacle_count > 0:
                        map[x][start] = 'O'
                        start += 1
                        obstacle_count -= 1
                    map[x][start] = '@'
                    map[x][y] = '.'
                    x, y = x, start
                    break
                start -= 1
        elif inst == '>':
            start = y
            obstacle_count = 0
            while y < len(map[0]):
                if map[x][start] == 'O':
                    obstacle_count += 1
                elif map[x][start] == '#':
                    break
                elif map[x][start] == '.':
                    while obstacle_count > 0:
                        map[x][start] = 'O'
                        start -= 1
                        obstacle_count -= 1
                    map[x][start] = '@'
                    map[x][y] = '.'
                    x, y = x, start
                    break
                start += 1
    total = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'O':
                total += 100*i + j
    print(total)


def dfs_vert(l, r, input, dx, dy, collect):
    lx, ly = l
    rx, ry = r
    rnx, rny = rx+dx, ry+dy
    # no bound checking as we will run into a wall first
    if input[lx][ly] == '#' or input[rx][ry] == '#':
        return False
    if input[lx][ly] == '.' and input[rx][ry] == '.':
        return True
    collect.add((lx, ly))
    collect.add((rx, ry))
    rnx, rny = rx+dx, ry+dy
    lnx, lny = lx+dx, ly+dy
    if input[lnx][lny] == '#' or input[rnx][rny] == '#':
        return False
    if input[lnx][lny] == '.' and input[rnx][rny] == '.':
        return True
    left_input = (lnx, lny-1), (lnx, lny), input, dx, dy, collect
    right_input = (rnx, rny), (rnx, rny+1), input, dx, dy, collect

    if input[lnx][lny] == ']' and input[rnx][rny] == '[':
        left_arm = dfs_vert(*left_input)
        right_arm = dfs_vert(*right_input)
        return left_arm and right_arm

    if input[lnx][lny] == '[' and input[rnx][rny] == ']':
        return dfs_vert((lnx, lny), (rnx, rny), input, dx, dy, collect)

    if input[lnx][lny] == ']':
        return dfs_vert(*left_input)

    return dfs_vert(*right_input)


def dfs_side(x, y, input, dx, dy, collect):
    nx, ny = x+dx, y+dy
    # no bound checking as we will run into a wall first
    if input[nx][ny] == '#':
        return False
    if input[nx][ny] == '.':
        return True
    collect.add((nx, ny))

    return dfs_side(nx, ny, input, dx, dy, collect)


def adjust_all_points2(points, dx, dy, input):
    mapping = defaultdict(str)
    for x, y in points:
        nx, ny = x+dx, y+dy
        mapping[(nx, ny)] = input[x][y]
        input[x][y] = '.'
    for k, v in mapping.items():
        x, y = k
        input[x][y] = v


def part2():
    input = read_input()
    map = []
    instructions = ''
    read_map = True
    mp = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }
    for i in range(len(input)):
        if not input[i]:
            read_map = False
            continue
        if read_map:
            start = [x for x in input[i]]
            new_section = []
            for item in start:
                if item == '#':
                    new_section.append('#')
                    new_section.append('#')
                elif item == 'O':
                    new_section.append('[')
                    new_section.append(']')
                elif item == '.':
                    new_section.append('.')
                    new_section.append('.')
                else:
                    new_section.append('@')
                    new_section.append('.')
            map.append(new_section)
        else:
            instructions += input[i]
    x, y = None, None
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                x, y = i, j
                break
        if x and y:
            break

    for inst in instructions:
        dx, dy = mp[inst]
        nx, ny = dx+x, dy+y
        if nx < 0 or ny < 0 or nx >= len(map) or ny >= len(map[0]) or map[nx][ny] == '#':
            continue
        if map[nx][ny] == '.':
            map[nx][ny] = '@'
            map[x][y] = '.'
            x, y = nx, ny
        else:
            if inst == '<' or inst == '>':
                collect = set([(nx, ny)])
                res = dfs_side(nx, ny, map, dx, dy, collect)
                if res:
                    adjust_all_points2(collect, dx, dy, map)
                    map[nx][ny] = '@'
                    map[x][y] = '.'
                    x, y = nx, ny
            else:
                points = ((nx, ny), (nx, ny +
                                     1)) if map[nx][ny] == '[' else ((nx, ny-1), (nx, ny))
                collect = set()
                res = dfs_vert(*points, map, dx, dy, collect)
                if res:
                    adjust_all_points2(collect, dx, dy, map)
                    map[nx][ny] = '@'
                    map[x][y] = '.'
                    x, y = nx, ny
    total = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '[':
                total += 100*i + j

    print('\n')
    for k in map:
        print(''.join(k))
    print(total)


part1()
part2()
