import math
import sys
import unittest
from collections import defaultdict, deque


def get_code_int(binary_string, pos, bits):
    code_bin, pos = get_code_bin(binary_string, pos, bits)
    code = int(code_bin, 2)
    return code, pos


def get_code_bin(binary_string, pos, bits):
    return binary_string[pos:pos + bits], pos+bits


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    code = ""
    with open(filename) as openfileobject:
        for line in openfileobject:
            code = line.strip()

    binarys = []
    for h in code:
        binarys.append(format(int(h,16), "04b"))

    binary_string = "".join(binarys)
    pos = 0

    _, vsum, nums = parse_from_pos(binary_string, pos, sys.maxsize)

    return vsum if part == 1 else nums[0]


def parse_from_pos(binary_string, pos, packets_to_parse):
    ver_sum = 0
    parsed_numbers = []
    while pos<len(binary_string)-1 and packets_to_parse > 0:
        packets_to_parse -= 1
        if len(binary_string)-pos <= 7 and binary_string[pos] == '0':
            break
        version, pos = get_code_int(binary_string, pos, 3)
        ver_sum += version
        dtype, pos = get_code_int(binary_string, pos, 3)
        print(f'ver: {version}')
        print(f'type: {dtype}')

        if dtype == 4:
            fbit = 1
            totbin = ""
            while fbit:
                fbit, pos = get_code_int(binary_string, pos, 1)
                litval, pos = get_code_bin(binary_string, pos, 4)
                totbin += litval
            print(f'litval: {int(totbin, 2)}')
            parsed_numbers.append(int(totbin, 2))
            #pos += (4 - (pos % 4))  # ff to next 4bit word
        else:
            length_type_id, pos = get_code_int(binary_string, pos, 1)
            new_nums = []
            if length_type_id:
                # 11bits = number of subpackets
                number_of_subpackets,pos = get_code_int(binary_string, pos, 11)
                print(f'num subpackets: {number_of_subpackets}')
                pos, more_versum, new_nums = parse_from_pos(binary_string, pos,number_of_subpackets)
                ver_sum += more_versum

            else:
                # 15 bits length of subpackets
                length_of_subpackets,pos = get_code_int(binary_string, pos, 15)
                print(f'subpackets {length_of_subpackets} bits')
                new_bin_str,pos = get_code_bin(binary_string, pos, length_of_subpackets)

                _, more_versum, new_nums = parse_from_pos(new_bin_str, 0, sys.maxsize)
                ver_sum += more_versum

            match dtype:
                case 0:
                    parsed_numbers.append(sum(new_nums))
                case 1:
                    parsed_numbers.append(math.prod(new_nums))
                case 2:
                    parsed_numbers.append(min(new_nums))
                case 3:
                    parsed_numbers.append(max(new_nums))
                case 5:
                    parsed_numbers.append(1 if new_nums[0] > new_nums[1] else 0)
                case 6:
                    parsed_numbers.append(1 if new_nums[0] < new_nums[1] else 0)
                case 7:
                    parsed_numbers.append(1 if new_nums[0] == new_nums[1] else 0)

    return pos, ver_sum, parsed_numbers


part1 = solve(1, False)
part2 = solve(2, False)
print()
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
