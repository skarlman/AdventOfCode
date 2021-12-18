import unittest
from collections import defaultdict, deque


class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right



def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    contents = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            start = stack.pop()
            contents.append((len(stack), f'{start}|{string[start + 1:i]}', string[start + 1: i]))

    contents.sort(key=lambda x: x[0])

    tree = dict()
    # depth, root_key, content = contents.pop()
    # current_node = Node(root_key)
    # tree[root_key] = current_node

    while contents:
        depth, key, content = contents.pop()
        start_i, key = key.split('|')

        n1 = Node()

        if content[0].isnumeric():
            n1.left = int(content.split(',')[0])

        if content[-1].isnumeric():
            n1.right = int(content.split(',')[-1])

        if n1.left == None:
            c = 1
            ptr = 1
            while c:
                if content[ptr] == '[':
                    c+=1
                elif content[ptr] == "]":
                    c-=1
            left_key=f'{depth}|{content[0:ptr]}'
            n1.left=tree[left_key]

        if n1.right == None:

    print(contents)


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    # TODO put solution here
    # with open(filename) as openfileobject:
    #     for line in openfileobject:
    #         tline = line.strip()
    #
    #         pass

    # example = "[[[[[9,8],1],2],3],4]"
    example ="[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"

    parts = list(parenthetic_contents(example))

    return None


print(solve(1, True))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
