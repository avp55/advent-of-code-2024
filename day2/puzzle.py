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


def line_safe(line):
    incr = False
    decr = False
    for i in range(len(line)):
        if i == 0:
            continue
        prev = line[i-1]
        cur = line[i]
        rang = abs(cur-prev)
        if not (1 <= rang <= 3):
            return False
        if prev < cur:
            if decr:
                return False
            incr = True
        if prev > cur:
            if incr:
                return False
            decr = True
    return True


def part1():
    input = read_input()
    safe = 0
    for line in input:
        line = line.split(' ')

        line = [int(x) for x in line]
        if line_safe(line):
            safe += 1
    print(safe)


def part2():
    input = read_input()
    safe = 0
    for line in input:
        line = [int(x) for x in line.split(' ')]
        if line_safe(line):
            safe += 1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i+1:]
                if line_safe(new_line):
                    safe += 1
                    break

    print(safe)


part1()
part2()
