import sys
import unittest
import timeit

def smart_solution():
    #https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/7.py

    filename = "input.txt"

    X = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            if not X:
                X = [int(x) for x in line.split(',')]

    X.sort()
    T = X[len(X) // 2]
    ans = 0

    def C2(d):
        # binomial coefficient (d+1 choose 2)
        # 1+2+3+...+d ~ d**2. d terms, which average (d+1)/2.
        return d * (d + 1) / 2

    best = 1e9
    for med in range(2000):
        score = 0
        for x in X:
            d = abs(x - med)
            score += C2(d)
        if score < best:
            best = score
    return best

def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    numbers = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            if not numbers:
                numbers = [int(x) for x in line.split(',')]

    max_num = max(numbers)

    positions = [0] * (max_num + 1)

    left = [0] * (max_num + 1)
    right = [0] * (max_num + 1)

    for n in numbers:
        positions[n] += 1

    lowest = sys.maxsize
    l_increased = False
    r_increased = False


    for i in range(1, max_num + 1, 1):
        j = max_num - i

        if part == 1:
            left[i] = left[i - 1] + sum(positions[0:i])
            right[j] = right[j + 1] + sum(positions[j + 1:])
        else:
            left[i] = left[i - 1] + sum((x * (i - ndx) for ndx, x in enumerate(positions[0:i])))
            right[j] = right[j + 1] + sum(x * (ndx + 1) for ndx, x in enumerate(positions[j + 1:]))

        if left[i] != 0 and right[i] != 0:
            if lowest >= left[i] + right[i]:
                lowest = left[i] + right[i]
            else:
                l_increased = True

        if left[j] != 0 and right[j] != 0:
            if lowest >= left[j] + right[j]:
                lowest = left[j] + right[j]
            else:
                r_increased = True

        if l_increased and r_increased:
            return lowest

    return lowest



# print(solve(2, False))

print("Smart solution:")
print(timeit.timeit("smart_solution()", globals=locals(), number=100))
print("My solution:")
print(timeit.timeit("solve(2, False)", globals=locals(), number=100))

class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(359648, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(37, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(100727924, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(168, solve(2, True), "Part 2 example")
