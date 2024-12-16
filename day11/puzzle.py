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


def part1():
    input = convert_line_to_nums(read_input()[0])
    # 0->1
    # even number of digits, split in half
    # else * 2024
    for _ in range(25):
        new_input = []
        for x in input:
            sdigit = str(x)
            if x == 0:
                new_input.append(1)
            elif len(sdigit) % 2 == 0:
                center = len(sdigit) // 2
                new_input.append(int(sdigit[center:]))
                new_input.append(int(sdigit[:center]))
            else:
                new_input.append(x*2024)
        input = new_input
    print(len(input))


def part2():
    input = convert_line_to_nums(read_input()[0])
    mp = defaultdict(int)
    for k in input:
        mp[k] += 1
    for k in range(75):
        new_mp = defaultdict(int)
        for x, v in mp.items():
            sdigit = str(x)
            if x == 0:
                new_mp[1] += v
            elif len(sdigit) % 2 == 0:
                center = len(sdigit) // 2
                new_mp[int(sdigit[center:])] += v
                new_mp[int(sdigit[:center])] += v
            else:
                new_mp[(x*2024)] += v
        mp = new_mp
    print(sum(mp.values()))


part1()
part2()
