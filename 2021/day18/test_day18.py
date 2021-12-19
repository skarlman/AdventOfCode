import unittest
from collections import defaultdict, deque


class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def build_tree(string):
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
    _, root_key, _ = contents[0]

    while contents:
        depth, key, content = contents.pop()
        start_i, _ = key.split('|')
        start_i = int(start_i)
        n1 = Node()

        if content[0].isnumeric():
            n1.left = int(content.split(',')[0])

        if content[-1].isnumeric():
            n1.right = int(content.split(',')[-1])

        midpoint = 0
        if n1.left == None:
            c = 1
            ptr = 1
            while c:
                if content[ptr] == '[':
                    c += 1
                elif content[ptr] == "]":
                    c -= 1
                ptr += 1

            left_key = f'{start_i + 1}|{content[1:ptr - 1]}'
            n1.left = tree[left_key]
            midpoint = ptr

        if n1.right == None:
            if midpoint == 0:
                ptr = 0
                while content[ptr] != '[':
                    ptr += 1

                midpoint = ptr - 1
            right_key = f'{start_i + midpoint + 2}|{content[midpoint + 2:-1]}'

            n1.right = tree[right_key]

        tree[key] = n1

    return tree[root_key]


def print_tree(node):
    if isinstance(node, int):
        return str(node)
    else:
        return f'[{print_tree(node.left)},{print_tree(node.right)}]'


def push_down_ur(node, number):
    if isinstance(node.left, int):
        node.left += number
    else:
        push_down_ur(node.left, number)


def push_down_ul(node, number):
    if isinstance(node.right, int):
        node.right += number
    else:
        push_down_ul(node.right, number)


def explode(node, level):
    if level == 4:
        return node.left, node.right, False

    ul,ur,has_updated = 0,0,False

    if not isinstance(node.left, int):

        ul, ur, has_updated = explode(node.left, level + 1)
        if ur != 0 and ul !=0 and has_updated==False:
            node.left = 0

        if ur != 0:
            # push down right
            if isinstance(node.right, int):
                node.right += ur
            else:
                push_down_ur(node.right, ur)
            return ul, 0, ul == 0

        if ul != 0:
            return ul, 0, has_updated

    if has_updated:
        return 0, 0, True


    if not isinstance(node.right, int):

        ul, ur, has_updated = explode(node.right, level + 1)

        if ur != 0 and ul != 0 and has_updated == False:
            node.right = 0

        if ul != 0:
            # push down left
            if isinstance(node.left, int):
                node.left += ul
            else:
                push_down_ul(node.left, ul)

            return 0, ur, ur == 0

    return 0, ur, has_updated


def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    inputrows = []
#    with open(filename) as openfileobject:
#        for line in openfileobject:
#            tline = line.strip()
#            root_node = build_tree(tline)
#            reconstructed = print_tree(root_node)

#            if tline != reconstructed:
#                print(" - !!! -- Not equal -- !!! -")
#                print(tline)
#                print(reconstructed)
#                print("-----------------------------")

    example = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    # example ="[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    # example = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    root_node = build_tree(example)
    reconstructed = print_tree(root_node)

    if example != reconstructed:
        print(" - !!! -- Not equal -- !!! -")
        print(example)
        print(reconstructed)
        print("-----------------------------")

    ul,ur,has_updated = explode(root_node,0)

    print(f'example: {example}')
    print(f'explode: {print_tree(root_node)}')



    return None


print(solve(1, False))


class AocTest(unittest.TestCase):
    def test_part_a_real(self):
        self.assertEqual(4421, solve(1, False), "Part 1 REAL")

    def test_part_a_example(self):
        self.assertEqual(5, solve(1, True), "Part 1 example")

    def test_part_b_real(self):
        self.assertEqual(18674, solve(2, False), "Part 2 REAL")

    def test_part_b_example(self):
        self.assertEqual(12, solve(2, True), "Part 2 example")
