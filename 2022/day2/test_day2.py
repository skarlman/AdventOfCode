import unittest
from collections import defaultdict, deque


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    total = 0

    # TODO put solution here
    if part == 1:
        with open(filename) as openfileobject:
            for line in openfileobject:
                a, b = line.strip().split(' ')
                score = 0

                if b == 'Y':
                    score += 2
                    if a == 'A':
                        score += 6
                    elif a == 'B':
                        score += 3
                elif b == 'X':
                    score += 1
                    if a == 'C':
                        score += 6
                    elif a == 'A':
                        score +=3
                elif b == 'Z':
                    score += 3
                    if a == 'B':
                        score += 6
                    elif a == 'C':
                        score += 3


                total += score

            return total
    else:
        ROCK = 'A'
        PAPER = 'B'
        SCISSORS = 'C'

        LOSE = 'X'
        DRAW = 'Y'
        WIN = 'Z'

        Points_Rock = 1
        Points_Paper = 2
        Points_Scissors = 3


        with open(filename) as openfileobject:
            for line in openfileobject:
                opponent, me = line.strip().split(' ')
                score = 0

                if (opponent == ROCK):
                    if me == LOSE:
                        score += Points_Scissors
                    elif me == DRAW:
                        score += 3
                        score += Points_Rock
                    else:
                        score += 6
                        score += Points_Paper
                elif opponent == SCISSORS:
                    if me == LOSE:
                        score += Points_Paper
                    elif me == DRAW:
                        score += 3
                        score += Points_Scissors
                    else:
                        score += 6
                        score += Points_Rock
                elif opponent == PAPER:
                    if me == LOSE:
                        score += Points_Rock
                    elif me == DRAW:
                        score += Points_Paper
                        score += 3
                    else:
                        score +=6
                        score += Points_Scissors
                total += score

            return total

    # if part == 2:
    #     return sum(v for k, v in sorted(elves.items(), key=lambda item: item[1])[-3:])


print(solve(2, False))

# class AocTest(unittest.TestCase):
#     def test_part_a_real(self):
#         self.assertEqual(4421, solve(1, False), "Part 1 REAL")
#
#     def test_part_a_example(self):
#         self.assertEqual(5, solve(1, True), "Part 1 example")
#
#     def test_part_b_real(self):
#         self.assertEqual(18674, solve(2, False), "Part 2 REAL")
#
#     def test_part_b_example(self):
#         self.assertEqual(12, solve(2, True), "Part 2 example")
