import math
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


def state(pointer, instructions, registers, combo):
    if pointer >= len(instructions):
        return (pointer, [])
    op = instructions[pointer]
    num = instructions[pointer + 1]
    outputs = []
    next_pointer = pointer + 2
    combo = combo[num] if num < 4 else registers[combo[num]]
    if op == 0:
        registers[0] = int(registers[0] / (2**combo))
    elif op == 1:
        registers[1] ^= num
    elif op == 2:
        registers[1] = combo % 8
    elif op == 3:
        if registers[0] != 0:
            next_pointer = num
    elif op == 4:
        registers[1] ^= registers[2]
    elif op == 5:
        outputs.append(combo % 8)
    elif op == 6:
        registers[1] = int(registers[0] / (2**combo))
    elif op == 7:
        registers[2] = int(registers[0] / (2**combo))
    else:
        raise Exception("op not implemented")
    return (next_pointer, outputs)


def part1():
    # moves by 2 except for jump
    # halts if it reads past input
    input = read_input()
    # 0 division - numerator A register, divisor is 2^(combo operant) (int) - result to A register
    # 1 XOR of B and literal operand
    # 2 combo operand % 8 - writes to b register
    # 3 does nothing if A=0, else it jumps to value of literal operand, no increment after jump
    # 4 XOR of B and C and puts in B
    # 5 combo operand % 8, outputs value
    # 6 like 0 but result is stored in B
    # 7like 0 but result is stored in C
    combo = [0, 1, 2, 3, 0, 1, 2]
    registers = [0, 0, 0]
    instructions = []
    for line in input:
        if line.startswith("Register"):
            reg = line.split("Register ")[1][0]
            reg_value = int(line.split(": ")[1])
            if reg == "A":
                registers[0] = reg_value
            elif reg == "B":
                registers[1] = reg_value
            else:
                registers[2] = reg_value
        elif line.startswith("Program:"):
            instructions = [int(x) for x in line[9:].split(",")]
    p = 0
    output = []
    while p < len(instructions):
        next_p, collected = state(p, instructions, registers, combo)
        p = next_p
        output += collected
    print(",".join([str(x) for x in output]))


def initialize():
    input = read_input()
    registers = [0, 0, 0]
    instructions = []
    for line in input:
        if line.startswith("Register"):
            reg = line.split("Register ")[1][0]
            reg_value = int(line.split(": ")[1])
            if reg == "A":
                registers[0] = reg_value
            elif reg == "B":
                registers[1] = reg_value
            else:
                registers[2] = reg_value
        elif line.startswith("Program:"):
            instructions = [int(x) for x in line[9:].split(",")]
    return registers, instructions


def dfs(position, start, combo, size):
    if position >= size + 1:
        return -1
    output = []
    iterator = 8 ** (16 - position)
    space = start + (8 ** (16 - position + 1)) + 1
    for i in range(start, space, iterator):
        registers, instructions = initialize()
        registers[0] = i
        p = 0
        output = []
        while p < len(instructions):
            next_p, collected = state(p, instructions, registers, combo)
            p = next_p
            output += collected
        if output[-position] == instructions[-position]:
            if position == size:
                return i
            result = dfs(position + 1, i, combo, size)
            if result != -1:
                return result
    return -1


# To get X digits, A has to be a minimum of 8^(X-1)
# 262144


def part2():
    combo = [0, 1, 2, 3, 0, 1, 2]
    # Looks like this can start from 0 and still be fast, doesn't have to be 8**15
    print(dfs(1, 0, combo, 16))


def testing_part2():
    combo = [0, 1, 2, 3, 0, 1, 2]
    for i in range(164516454463176, 16451645446317600 + 15, 1):
        registers, instructions = initialize()
        registers[0] = i
        p = 0
        output = []
        while p < len(instructions):
            next_p, collected = state(p, instructions, registers, combo)
            p = next_p
            output += collected
        if len(output) != 16:
            break
        if output[1] != 4:
            break
        print(i, oct(i), output, [oct(x) for x in output])


part1()
part2()
# Scratchpad during thinking below
#
#
#
# 8**15


# print(8**(16-1))
164516454348488
# print(math.log(35184372088832, 8))

# 8**15

# Number is between print(8**15 + (3*(8**15)))  # 140737488355328 0 and print(8**15 + (4*(8**15)))  # 175921860444160 1
# print('Initial band for 16 digits', 35184372088832)
# print('Increment for second', 39582418599936)
# print('Starting for last 0', 140737488355328)
# print((140737488355328-35184372088832) / 35184372088832)
# print(140737488355328+39582418599936)
# part2()
# Number is from 536561674354688 to 576144092954624 maybe?
536561674354688
# print(576144092954624-536561674354688)
39582418599936
# print(8**13)
# part2()

162727720910848
# every 8**14 the second number switches

# 8^(16-3) = 549755813888

# print(8**15)
# 4, 398, 046, 511, 104
# print(8**14)  # 4398046511104
# print(8**15 + (3*(8**15)))
# print((8**15 + (3*(8**15)) + 4398046511104))
# print(8**15 + (3*(8**15)))

# print(140737488355328 + (8**14))
# size 3 every 8
# second number changes every 64 for size 4

# 8^(size-2)

# print(8**15)  # 35184372088832 4
# print(8**15 + (1*(8**15)))  # 70368744177664 6
# print(8**15 + (2*(8**15)))  # 105553116266496 7
# print(8**15 + (3*(8**15)))  # 140737488355328 0
# print(8**15 + (4*(8**15)))  # 175921860444160 1
# part2()
# print(175921860444160-140737488355328)
# 35,184,372,088,832

# 30,786,325,577,728
# 281474976710655 - last 16 digit
# 281474976710656 - first 17 digit
# 16 lenght number
# every 8 ^ (len(digits)-1) last digit changes
# 4-6-7-0-1-2-3 (Then next queue starts)

# 4-8-8-8-24

# every 64, last number changes

# print((8**16)-(8**15))

# *8 for next digit
# 2 digit at 8
# 3 digit at 64
# 4 digit    512
# 5 digit at 4,096
# 6 digit at 32,768
# 7 digit at 262,144
# 8 digit at 32768
# 9 digit at 32768
# 10 digitat 32768

# 164516454463168
