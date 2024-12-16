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


def swapper(input):
    end = len(input) - 1
    while end > -1:
        if input[end] != '.':
            break
        end -= 1
    start = 0
    while start < end:
        while start < end and input[start] != '.':
            start += 1
        while end > start and input[end] == '.':
            end -= 1
        input[start], input[end] = input[end], input[start]


def next_num_rev(input, move):
    while move > -1:
        if input[move] != '.':
            break
        move -= 1
    end = move
    while move > -1:
        if input[move] == '.' or input[move] != input[end]:
            break
        move -= 1
    if input[move] == '.' or input[move] != input[end]:
        move += 1
    return (move, end)


def next_empty_block(input, move):
    while move < len(input):
        if input[move] == '.':
            break
        move += 1
    if move >= len(input):
        return (-1, -1)
    start = move
    while move < len(input):
        if input[move] != '.':
            break
        move += 1
    if move < len(input) and input[move] != '.':
        move -= 1
    return (start, move)


def enumerate_empty(input):
    start = 0
    opts = []
    while start < len(input):
        es, ee = next_empty_block(input, start)
        if es == -1:
            break
        opts.append((ee-es+1, es, ee))
        start = ee+1
    return opts


def part1():
    line = read_input()
    line = line[0]
    net = []
    is_free_space = True
    c = '.'
    idn = 0
    for c in line:
        is_free_space = not is_free_space
        count = int(c)
        while count > 0:
            if is_free_space:
                net.append('.')
            else:
                net.append(idn)
            count -= 1
        if not is_free_space:
            idn += 1
    swapper(net)
    total = 0
    for i, c in enumerate(net):
        if c == '.':
            break
        total += (i*int(c))
    print(total)

# very sloow


def part2():
    line = read_input()
    line = line[0]
    net = []
    is_free_space = True
    c = '.'
    idn = 0
    for c in line:
        is_free_space = not is_free_space
        count = int(c)
        while count > 0:
            if is_free_space:
                net.append('.')
            else:
                net.append(idn)
            count -= 1
        if not is_free_space:
            idn += 1
    rear = len(net)-1
    empty_spots = enumerate_empty(net)
    while rear > -1:
        ns, ne = next_num_rev(net, rear)
        num_size = ne-ns+1
        idx = -1
        for i, (ln, s, e) in enumerate(empty_spots):
            if ln >= (num_size) and e < ns:
                idx = i
                break
        if idx == -1:
            rear = ns-1
            continue
        _, es, en = empty_spots[idx]
        while num_size > 0:
            net[es], net[ne] = net[ne], net[es]
            es += 1
            ne -= 1
            num_size -= 1
        rear = ns-1
        empty_spots = enumerate_empty(net)

    # print(net)
    total = 0
    for i, c in enumerate(net):
        if c == '.':
            continue
        total += (i*int(c))
    print(total)


part2()
