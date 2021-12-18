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
    _, root_key,_ = contents[0]

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
                    c+=1
                elif content[ptr] == "]":
                    c-=1
                ptr +=1

            left_key=f'{start_i+1}|{content[1:ptr-1]}'
            n1.left=tree[left_key]
            midpoint = ptr


        if n1.right == None:
            if midpoint == 0:
                c = 1
                ptr = 1
                while c:
                    if content[ptr] == '[':
                        c += 1
                    elif content[ptr] == "]":
                        c -= 1
                    ptr += 1
                midpoint = ptr
            right_key = f'{start_i+midpoint+2}|{content[midpoint + 2:-1]}'

            n1.right = tree[right_key]

        tree[key] = n1

    return (tree, root_key)


def print_tree(node):
    if isinstance(node.left, int):
        print(node.left)
    else:
        print_tree(node.left)

    if isinstance(node.right, int):
        print(node.right)
    else:
        print_tree(node.right)






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

    tree, root_key = build_tree(example)

    print_tree(tree[root_key])


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
