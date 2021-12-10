import unittest


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    p1_scores = {}
    p1_scores[')'] = 3
    p1_scores[']'] = 57
    p1_scores['}'] = 1197
    p1_scores['>'] = 25137

    p2_scores = {}
    p2_scores['('] = 1
    p2_scores['['] = 2
    p2_scores['{'] = 3
    p2_scores['<'] = 4


    lines = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            if tline:
                lines.append(tline)


    pairs = {}
    pairs[')'] = '('
    pairs[']'] = '['
    pairs['}'] = '{'
    pairs['>'] = '<'


    p1_score = 0
    p2_row_scores = []
    for l in lines:
        stackare = []
        incomlete = True

        for c in l:
            if c in pairs:
                if stackare[-1] != pairs[c]:
                    p1_score += p1_scores[c]
                    incomlete = False
                    break
                else:
                    stackare.pop()
            else:
                stackare.append(c)
        if incomlete:
            p2_part_score = 0
            for c in stackare[::-1]:
                p2_part_score *= 5
                p2_part_score += p2_scores[c]
            p2_row_scores.append(p2_part_score)




    if part == 1:
        return p1_score
    else:
        return sorted(p2_row_scores)[len(p2_row_scores)//2]



print(solve(2, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
