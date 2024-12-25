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


def determine_output(wire1_value, wire2_value, op):
    wire_output = 0
    if op == "AND":
        wire_output = 1 if (wire1_value == 1 and wire2_value == 1) else 0
    elif op == "OR":
        wire_output = 0 if (wire1_value == 0 and wire2_value == 0) else 1
    elif op == "XOR":
        wire_output = (
            1
            if (
                (wire1_value == 1 and wire2_value == 0)
                or (wire1_value == 0 and wire2_value == 1)
            )
            else 0
        )
    return wire_output


def part1():
    mp = defaultdict(int)
    input = read_input()
    wait = []
    for line in input:
        if ":" in line:
            wire_id = line.split(":")[0]
            wire_num = line.split(": ")[1]
            mp[wire_id] = int(wire_num)
        elif "->" in line:
            line_split = line.split()
            wire_id_1, wire_id_2, op, wire_output_id = (
                line_split[0],
                line_split[2],
                line_split[1],
                line_split[4],
            )

            if wire_id_1 not in mp or wire_id_2 not in mp:
                wait.append((wire_id_1, wire_id_2, wire_output_id, op))
                continue
            wire1_value, wire2_value = int(mp[wire_id_1]), int(mp[wire_id_2])
            mp[wire_output_id] = determine_output(wire1_value, wire2_value, op)
    while wait:
        wait_again = []
        for wire1_id, wire2_id, output_wire_id, op in wait:
            if wire1_id not in mp or wire2_id not in mp:
                wait_again.append((wire1_id, wire2_id, output_wire_id, op))
                continue
            wire1_value, wire2_value = mp[wire1_id], mp[wire2_id]
            mp[output_wire_id] = determine_output(wire1_value, wire2_value, op)
        wait = wait_again
    output = ""
    keys = sorted(mp.keys(), reverse=True)
    for k in keys:
        if k[0] == "z":
            output += str(mp[k])
    print(int(output, 2))

    # AND = 1 if both 1 else 0
    # OR = at least 1 input is 1 else 0
    # XOR = 1 if inputs are different else 0
    # 1 0 or no value, wait until all values resolved


def print_x_y(mp):
    keys = sorted(mp.keys(), reverse=True)
    x = ""
    y = ""

    for k in keys:
        if k[0] == "x":
            x += str(mp[k])
        elif k[0] == "y":
            y += str(mp[k])
    cmb = [""] * max(len(x), len(y))
    # print(len(x), len(y), len(cmb))
    for i in range(len(x)):
        cmb[i] = str(int(x[i]) ^ int(y[i]))
    # print(int(x, 2))
    # print(int(y, 2))
    return bin(int(x, 2) + int(y, 2))[2:]


def part2():
    mp = defaultdict(int)
    input = read_input()
    wait = []
    correct_number = ""
    for line in input:
        if ":" in line:
            wire_id = line.split(":")[0]
            wire_num = line.split(": ")[1]
            mp[wire_id] = int(wire_num)
        elif not line:
            correct_number = print_x_y(mp)
        elif "->" in line:

            line_split = line.split()
            wire_id_1, wire_id_2, op, wire_output_id = (
                line_split[0],
                line_split[2],
                line_split[1],
                line_split[4],
            )
            if wire_id_1 not in mp or wire_id_2 not in mp:
                wait.append((wire_id_1, wire_id_2, wire_output_id, op))
                continue
            wire1_value, wire2_value = int(mp[wire_id_1]), int(mp[wire_id_2])
            mp[wire_output_id] = determine_output(wire1_value, wire2_value, op)
    while wait:
        wait_again = []
        print(wait)
        for wire1_id, wire2_id, output_wire_id, op in wait:
            if wire1_id not in mp or wire2_id not in mp:
                wait_again.append((wire1_id, wire2_id, output_wire_id, op))
                continue
            wire1_value, wire2_value = mp[wire1_id], mp[wire2_id]
            mp[output_wire_id] = determine_output(wire1_value, wire2_value, op)
        wait = wait_again
    output = ""
    keys = sorted(mp.keys(), reverse=True)
    for k in keys:
        if k[0] == "z":
            output += str(mp[k])
    print(correct_number)
    print(output)
    for i in range(len(output) - 1, -1, -1):
        if output[i] != correct_number[i]:
            spot = (len(output) - 1) - i
            print("wrong at", spot)
            return
    # print("out", output)
    # print(int(output, 2))
    # Determine which Zs are wrong
    # follow up - if pointing to x and y, cannot fix, must swap with another Z
    # else


part2()

# swap 1
# x10 AND y10 -> z10
# y10 XOR x10 -> htv


# ptd AND scj -> z21
# scj XOR ptd -> nks


# jtg OR trf -> z33
# y33 XOR x33 -> tkq


# wtc OR ndp -> z45


# jtg OR trf -> ghp

# tkq XOR mvc -> ghp
# htv XOR whd -> gpr
