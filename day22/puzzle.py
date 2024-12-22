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


def transition(x):
    step1 = (x ^ (x * 64)) % 16777216
    step2 = (step1 ^ int(step1 / 32)) % 16777216
    step3 = (step2 ^ (step2 * 2048)) % 16777216
    return step3


def part1():
    input = read_input()
    input = [int(x) for x in input]
    total = 0
    for num in input:
        num = num
        for _ in range(2000):
            num = transition(num)
        total += num
    print(total)


def form_consecutive_blocks(digits, start):
    if len(digits) < 4:
        return {}
    digit_map = {}
    for i in range(3, len(digits), 1):
        diff1 = digits[i - 3] - start if i - 3 == 0 else digits[i - 3] - digits[i - 4]
        diff2 = digits[i - 2] - digits[i - 3]
        diff3 = digits[i - 1] - digits[i - 2]
        diff4 = digits[i] - digits[i - 1]

        key = (diff1, diff2, diff3, diff4)
        if key in digit_map:
            continue
        digit_map[key] = digits[i]
    return digit_map


def form_consecutive_blocks2(digits, start):
    if len(digits) < 4:
        return {}
    digit_map = {}
    q = deque([(0, start)])
    for i in range(len(digits)):
        q.append((digits[i] - q[-1][1], digits[i]))
        while len(q) > 4:
            q.popleft()
        if len(q) < 4:
            continue
        key = tuple(x[0] for x in q)
        if key in digit_map:
            continue
        digit_map[key] = digits[i]
    return digit_map


def part2():
    # for each set of secret numbers, calculate all 4 transitions and put in map. Combine all into a set
    # iterate through all maps and see what the highest is.
    input = read_input()
    input = [int(x) for x in input]
    block_map = []
    keys = set()
    for num_original in input:
        num = num_original
        digits = []
        for _ in range(2000):
            num = transition(num)
            end_digit = int(str(num)[-1])
            digits.append(end_digit)
        blocks = form_consecutive_blocks2(digits, int(str(num_original)[-1]))
        block_map.append(blocks)
        for k in blocks.keys():
            keys.add(k)
    max_banana = 0
    for k in keys:
        attempt = 0
        for block in block_map:
            block.get(k, 0)
            attempt += block.get(k, 0)
        max_banana = max(max_banana, attempt)
    print(max_banana)


part1()
part2()
