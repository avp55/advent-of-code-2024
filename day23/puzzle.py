import os
from collections import defaultdict, Counter
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


def dfs(node, mp, visited, group, results, processed, size):
    if node in visited:
        return
    visited.add(node)
    group.append(node)
    if len(group) > size:
        sorted_group = sorted(group)
        key = "-".join(sorted_group)
        visited.remove(node)
        if key in processed:
            return
        processed.add(key)
        results.append(sorted_group)
        return
    for next in mp[node]:
        in_all = True
        for g in group:
            if next not in mp[g]:
                in_all = False
                break
        if not in_all:
            continue
        dfs(next, mp, visited, group[:], results, processed, size)


# de-ta
# de-ka

# ta-de
# ta-ka

# ka-de
# ka-ta


def part1():
    # bi directional
    # find groups of 3
    input = read_input()
    mp = defaultdict(set)
    for line in input:
        fr, to = line.split("-")
        mp[fr].add(to)
        mp[to].add(fr)
    processed = set()
    groups = []
    for k in mp:
        results = []
        dfs(k, mp, set(), [], results, processed, 2)
        for r in results:
            groups.append(r)
    filtered = [g for g in groups if g[0][0] == "t" or g[1][0] == "t" or g[2][0] == "t"]
    print(len(filtered))


def find_groups(mp, size):
    processed = set()
    groups = []
    for k in mp:
        results = []
        dfs(k, mp, set(), [], results, processed, size)
        for r in results:
            groups.append(r)
    return (len(groups), groups)


def part2():
    input = read_input()
    mp = defaultdict(set)
    for line in input:
        fr, to = line.split("-")
        mp[fr].add(to)
        mp[to].add(fr)
    lo = 1
    hi = len(mp)
    result = []
    while lo <= hi:
        mid = (lo + hi) // 2
        num, maybe_result = find_groups(mp, mid)
        if num == 0:
            hi = mid - 1
        else:
            result = maybe_result[0]
            lo = mid + 1
    print(",".join((sorted(result))))


# part1()
part2()
