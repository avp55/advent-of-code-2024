from math import floor
import os
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop
from functools import cmp_to_key


def read_input() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'part1.txt')
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def cmp(a, b, mpSm, mpBg):
    if a in mpSm and b in mpSm[a]:
        return -1
    if b in mpSm and a in mpSm[b]:
        return 1
    if b == a:
        return 0
    if a in mpBg and b in mpBg[a]:
        return 1
    if b in mpBg and a in mpBg[b]:
        return -1
    return 0


def part1():
    input = read_input()
    mpSm = defaultdict(set)
    mpBg = defaultdict(set)
    rows = []
    for line in input:
        if '|' in line:
            num1, num2 = line.split('|')
            num1, num2 = int(num1), int(num2)
            mpSm[num1].add(num2)
            mpBg[num2].add(num1)
        elif line:

            rows.append([int(x) for x in line.split(',')])
    total = 0
    for row in rows:
        sorted_list = sorted(row, key=cmp_to_key(
            lambda a, b: cmp(a, b, mpSm, mpBg)))
        if row == sorted_list:
            total += row[floor(len(row)/2)]
    print(total)


def part2():
    input = read_input()
    mpSm = defaultdict(set)
    mpBg = defaultdict(set)
    rows = []
    for line in input:
        if '|' in line:
            num1, num2 = line.split('|')
            num1, num2 = int(num1), int(num2)
            mpSm[num1].add(num2)
            mpBg[num2].add(num1)
        elif line:

            rows.append([int(x) for x in line.split(',')])
    total = 0
    for row in rows:
        sorted_list = sorted(row, key=cmp_to_key(
            lambda a, b: cmp(a, b, mpSm, mpBg)))
        if row != sorted_list:
            total += sorted_list[floor(len(sorted_list)/2)]
    print(total)


part1()
part2()
