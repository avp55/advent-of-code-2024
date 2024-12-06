import os
from collections import defaultdict


def read_input():
    input = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'input1.txt')
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def part1():
    l1, l2 = [], []
    input = (read_input())
    for line in input:
        line = line.split(' ')
        l1.append(int(line[0]))
        l2.append(int(line[-1]))
    l1.sort()
    l2.sort()
    dist = 0
    for i in range(len(l1)):
        dist += abs(l1[i]-l2[i])
    print(dist)


def part2():
    l1 = []
    appear = defaultdict(int)
    input = (read_input())
    for line in input:
        line = line.split(' ')
        l1.append(int(line[0]))
        appear[int(line[-1])] += 1
    dist = 0
    for i in range(len(l1)):
        dist += (l1[i] * appear[l1[i]])
    print(dist)


part1()
part2()
