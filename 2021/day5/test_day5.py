import unittest


def solve(part, useExample):
    filename = "testinput.txt" if useExample else "input.txt"


    walls = dict()

    ctr = 0

    with open(filename) as openfileobject:
        for line in openfileobject:
            f, t = line.split(' -> ')
            r1, c1 = [int(c) for c in f.split(',')]
            r2, c2 = [int(c) for c in t.split(',')]

            if c1 == c2:
                for i in range(min(r1, r2), max(r1, r2)+1):
                    el = (i, c1)
                    if el in walls:
                        walls[el] += 1
                        if walls[el] == 2:
                            ctr += 1
                    else:
                        walls[el] = 1
            elif r1==r2:
                for i in range(min(c1, c2), max(c1, c2)+1):
                    el = (r1, i)
                    if el in walls:
                        walls[el] += 1
                        if walls[el] == 2:
                            ctr += 1
                    else:
                        walls[el] = 1
            elif part==2:
                start_r = r1
                start_c = c1
                steps = abs(r2-r1)+1

                c_dir = 1 if c2 > c1 else -1
                r_dir = 1 if r2 > r1 else -1

                for i in range(steps):
                    el = (start_r+(i*r_dir), start_c+(i*c_dir))
                    if el in walls:
                        walls[el] += 1
                        if walls[el] == 2:
                            ctr += 1
                    else:
                        walls[el] = 1

    return ctr






class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False))

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True))


    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False))

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True))

