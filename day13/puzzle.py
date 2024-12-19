import numpy as np
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


def helper(a_count, b_count, x, y, xt, yt, mp, cache):
    key = (x, y)
    if key in cache:
        return cache[key]
    if a_count > 100 or b_count > 100:
        return float('inf')
    if x == xt and y == yt:
        return 0
    if x > xt or y > yt:
        return float('inf')
    xA = mp['a']['x']
    yA = mp['a']['y']

    xB = mp['b']['x']
    yB = mp['b']['y']
    cache[key] = min(3+helper(a_count+1, b_count, x+xA, y+yA, xt, yt, mp, cache),
                     1+helper(a_count, b_count+1, x+xB, y+yB, xt, yt, mp, cache))
    return cache[key]


def part1():
    # 3 tokens for B, 1 for A, each button can pressed at most 100 times
    input = read_input()
    total = 0
    for i in range(4, len(input), 4):
        button_a, button_b, prize, _ = (input[i-4:i])
        a_x = int(button_a.split(',')[0][12:])
        a_y = int(button_a.split(',')[1][3:])

        b_x = int(button_b.split(',')[0][12:])
        b_y = int(button_b.split(',')[1][3:])

        x_prize = int(prize.split(',')[0][9:])
        y_prize = int(prize.split(',')[1][3:])

        mp = {'a': {'x': a_x, 'y': a_y}, 'b': {'x': b_x, 'y': b_y}}
        res = helper(0, 0, 0, 0, x_prize, y_prize, mp, {})
        if res != float('inf'):
            total += res
    print(total)


def part2():
    input = read_input()
    total = 0
    i = 0
    while i < len(input):
        if not input[i]:
            i += 1
            continue
        if i+3 > len(input):
            break

        button_a, button_b, prize, = input[i:i+3]
        i += 4

        a_x = int(button_a.split(',')[0][12:])
        a_y = int(button_a.split(',')[1][3:])

        b_x = int(button_b.split(',')[0][12:])
        b_y = int(button_b.split(',')[1][3:])

        x_prize = int(prize.split(',')[0][9:])
        y_prize = int(prize.split(',')[1][3:])

        coeff = np.array([[a_x, b_x], [a_y, b_y]])
        prizes = np.array([x_prize, y_prize]) + 10000000000000
        results = np.linalg.solve(coeff, prizes).round()

        # https://numpy.org/doc/2.1/reference/generated/numpy.linalg.solve.html
        # Check that the solution is correct
        if (np.dot(coeff, results) == prizes).all():
            a, b = results.astype(int)
            total += a * 3 + b

    print(total)


part1()
part2()
