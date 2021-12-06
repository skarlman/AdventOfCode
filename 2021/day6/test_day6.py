import unittest


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    if part==1:
        totaldays = 18  if useExample else 80
    else:
        totaldays = 256 if useExample else 256
    numbers = []

    days = [0] * 9

    with open(filename) as openfileobject:
        for line in openfileobject:
            if not numbers:
                numbers = line.split(',')

    for num in numbers:
        days[int(num)] += 1

    for i in range(totaldays):
        today = days.pop(0)
        days[6] += today
        days.append(today)



    return sum(days)


result = solve(1,True)
print(result)

class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(376194, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(26, solve(1, True), "Part 1 example")


    def test_part_b_real(self):
        self.assertEqual(1693022481538, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(26984457539, solve(2, True), "Part 2 example")