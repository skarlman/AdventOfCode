import unittest
from collections import defaultdict, deque


def print_rope(rope):
    print()
    for row in range(11):
        print()
        for col in range(20):
            try:
                i = rope.index((row,col))
            except:
                i = -1
            if i == 0:
                i = "H"
            elif i == len(rope)-1:
                i = "T"

            print(i if (row,col) in rope else ".", end ="")

    print()


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read().strip()
        lines = [l.strip().split(' ') for l in openfileobject.readlines()]

    # H = (1,1)
    # T = (1,1)
    #
    # tail_visits = set()
    # tail_visits.add(T)
    #
    # for (dir, steps) in lines:
    #     for s in range(int(steps)):
    #         if dir == "R":
    #             H = (H[0], H[1] +1)
    #             if abs(H[1]-T[1]>1):
    #                 T = (H[0], H[1]-1)
    #         elif dir == "L":
    #             H = (H[0], H[1] -1)
    #             if abs(T[1]-H[1])>1:
    #                 T = (H[0], H[1]+1)
    #         elif dir == "U":
    #             H = (H[0]-1, H[1])
    #             if abs(H[0]-T[0])>1:
    #                 T = (H[0]+1, H[1])
    #         elif dir == "D":
    #             H = (H[0]+1, H[1])
    #             if abs(T[0]-H[0])>1:
    #                 T = (H[0]-1, H[1])
    #
    #         tail_visits.add(T)

    rope = [(10,10)]*10
    
    tail_visits = set()
    tail_visits.add(rope[-1])

    for (dir, steps) in lines:
        print(f" == {dir} {steps} ==")
        for s in range(int(steps)):
        
            if dir == "R":
                rope[0] = (rope[0][0], rope[0][1] +1)
            elif dir == "L":
                rope[0] = (rope[0][0], rope[0][1] -1)
            elif dir == "U":
                rope[0] = (rope[0][0]-1, rope[0][1])
            elif dir == "D":
                rope[0] = (rope[0][0]+1, rope[0][1])

            for knot_i in range(1,len(rope)):
                row_d = rope[knot_i-1][0] - rope[knot_i][0]
                col_d = rope[knot_i-1][1] - rope[knot_i][1]

                if row_d != 0:
                    row_d -= 1 if row_d > 0 else -1

                if col_d != 0:
                    col_d -= 1 if col_d > 0 else -1


                if row_d or col_d:
                    rope[knot_i] = (rope[knot_i-1][0] - row_d, rope[knot_i-1][1] - col_d)
                # else:
                #     rope[knot_i] = (rope[knot_i - 1][0] - row_d, rope[knot_i - 1][1] - col_d)
                # elif abs(row_d) > 0 or abs(col_d) > 0:
                #     rope[knot_i - 1] = (rope[knot_i][0] + row_d, rope[knot_i][1] + col_d)

                # if abs(rope[knot_i-1][1] - rope[knot_i][1] > 1):
                #         rope[knot_i] = (rope[knot_i-1][0], rope[knot_i-1][1] - 1)
                # elif abs(rope[knot_i][1] - rope[knot_i-1][1]) > 1:
                #         rope[knot_i] = (rope[knot_i-1][0], rope[knot_i-1][1] + 1)
                # elif abs(rope[knot_i-1][0] - rope[knot_i][0]) > 1:
                #         rope[knot_i] = (rope[knot_i-1][0] + 1, rope[knot_i-1][1])
                # elif abs(rope[knot_i][0] - rope[knot_i-1][0]) > 1:
                #         rope[knot_i] = (rope[knot_i-1][0] - 1, rope[knot_i-1][1])

            tail_visits.add(rope[-1])

            # print_rope(rope)


    return len(tail_visits)




print(f'Part 1: {solve(1, False)}')
# print(f'Part 2: {solve(2, True)}')



#
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
