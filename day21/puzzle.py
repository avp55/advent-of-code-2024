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


def normal_bfs(q, ex, ey, map, options_map):
    option_keys = options_map.keys()
    level = 0
    visited = set()
    while q:
        for _ in range(len(q)):
            x, y, cmds = q.popleft()
            if (x, y) == (ex, ey):
                return (level, [cmds + "A"])
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for opt in option_keys:
                ox, oy = options_map[opt]
                nx, ny = x + ox, y + oy
                if (
                    nx < 0
                    or ny < 0
                    or nx >= len(map)
                    or ny >= len(map[0])
                    or map[nx][ny] == "."
                ):

                    continue
                # meoWWWWWW
                q.append((nx, ny, cmds + opt))
        level += 1
    return (float("inf"), [])


def exhaustive_bfs(q, ex, ey, map, options_map):
    option_keys = options_map.keys()
    min_dist = float("inf")
    level = 0
    results = []
    while q:
        for _ in range(len(q)):
            x, y, cmds, visited = q.popleft()
            if (x, y) == (ex, ey) and level <= min_dist:
                min_dist = level
                results.append(cmds + "A")
                continue
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for opt in option_keys:
                ox, oy = options_map[opt]
                nx, ny = x + ox, y + oy
                if (
                    nx < 0
                    or ny < 0
                    or nx >= len(map)
                    or ny >= len(map[0])
                    or map[nx][ny] == "."
                ):

                    continue
                # meoWWWWWW
                q.append((nx, ny, cmds + opt, set(visited)))
        level += 1
    return (min_dist, results)


def find_final_length(keypad, dir_pad_to_coords, num_to_coord, seq):
    sx, sy = num_to_coord["A"]
    start_points = [(sx, sy, "")]
    for c in seq:
        ex, ey = num_to_coord[c]
        q = deque()
        for sx, sy, cmd in start_points:
            q.append((sx, sy, cmd, set()))
        dist, new_cmds = exhaustive_bfs(q, ex, ey, keypad, dir_pad_to_coords)
        if dist == float("inf"):
            raise Exception("Impossible")
        start_points = [(ex, ey, x) for x in new_cmds]

    first_direction_cmds = [x[2] for x in start_points]
    robot2 = [[".", "^", "A"], ["<", "v", ">"]]
    num_to_coord2 = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

    all_points = set()
    for seq in first_direction_cmds:
        sx, sy = num_to_coord2["A"]
        start_points = [(sx, sy, "")]
        for c in seq:
            ex, ey = num_to_coord2[c]
            q = deque()
            for sx, sy, cmd in start_points:
                q.append((sx, sy, cmd, set()))
            dist, new_cmds = exhaustive_bfs(q, ex, ey, robot2, dir_pad_to_coords)
            if dist == float("inf"):
                raise Exception("Impossible")
            start_points = [(ex, ey, x) for x in new_cmds]
        for point in start_points:
            all_points.add(point[2])
    all_points_fn = set()
    for seq in all_points:
        sx, sy = num_to_coord2["A"]
        start_points = [(sx, sy, "")]
        for c in seq:
            ex, ey = num_to_coord2[c]
            q = deque()
            for sx, sy, cmd in start_points:
                q.append((sx, sy, cmd))
            dist, new_cmds = normal_bfs(q, ex, ey, robot2, dir_pad_to_coords)
            if dist == float("inf"):
                raise Exception("Impossible")
            start_points = [(ex, ey, x) for x in new_cmds]
        for point in start_points:
            all_points_fn.add(point[2])

    lst = list(all_points_fn)
    lst = sorted(lst, key=len)
    final_len = len(lst[0])
    return final_len


def part1():
    # 789
    # 456
    # 123
    # .OA
    # start at A at bottom right
    input = read_input()
    keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [".", "0", "A"]]
    dir_pad_to_coords = {"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)}
    num_to_coord = {
        "0": (3, 1),
        "A": (3, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
    }
    total = 0
    for line in input:
        number = int(line[0 : len(line) - 1])
        line_len = find_final_length(keypad, dir_pad_to_coords, num_to_coord, line)
        total += number * line_len
    print(total)


def part2():
    read_input()


part1()
