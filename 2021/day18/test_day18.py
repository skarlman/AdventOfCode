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

            #todo check that there are no more parts
        expected_len = 1 #comma
        if isinstance(n1.left, int):
            expected_len += len(str(n1.left))
        else:
            expected_len += len(left_key.split('|')[1])+2

        if isinstance(n1.right, int):
            expected_len += len(str(n1.right))
        else:
            expected_len += len(right_key.split('|')[1])+2

        assert(expected_len==len(content))
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


def split_node(node):
    has_split = False

    if isinstance(node.left, int):
        if node.left > 9:
            new_node = Node()
            new_node.left = node.left // 2
            new_node.right = node.left - new_node.left
            node.left = new_node
            return True
    else:
        has_split = split_node(node.left)

    if has_split:
        return has_split

    if isinstance(node.right, int):
        if node.right > 9:
            new_node = Node()
            new_node.left = node.right // 2
            new_node.right = node.right - new_node.left
            node.right = new_node
            return True
    else:
        has_split = split_node(node.right)

    return has_split


def explode(node, level):
    if level == 4:
        return node.left, node.right, False

    ul, ur, has_updated = None, None, False

    if not isinstance(node.left, int):

        ul, ur, has_updated = explode(node.left, level + 1)
        if ur != None and ul != None and has_updated == False:
            node.left = 0

        if ur != None:
            # push down right
            if isinstance(node.right, int):
                node.right += ur
            else:
                push_down_ur(node.right, ur)
            return ul, None, True

        if ul != None:
            return ul, None, has_updated

    if has_updated:
        return None, ur, True

    if not isinstance(node.right, int):

        ul, ur, has_updated = explode(node.right, level + 1)

        if ur != None and ul != None and has_updated == False:
            node.right = 0

        if ul != None:
            # push down left
            if isinstance(node.left, int):
                node.left += ul
            else:
                push_down_ul(node.left, ul)

            return None, ur, True

    return ul, ur, has_updated


def get_magnitude(node):

    leftsum = 3 * node.left if isinstance(node.left, int) else 3 * get_magnitude(node.left)
    rightsum = 2 * node.right if isinstance(node.right, int) else 2 * get_magnitude(node.right)

    return leftsum+rightsum



def solve(part, useExample):
    filename = "exampleinput.txt" if useExample else "input.txt"

    inputrows = []
    with open(filename) as openfileobject:
        for line in openfileobject:
            tline = line.strip()
            root_node = build_tree(tline)
            reconstructed = print_tree(root_node)

            if tline != reconstructed:
                print(" - !!! -- Not equal -- !!! -")
                print(tline)
                print(reconstructed)
                print("-----------------------------")
            inputrows.append(tline)

    last_row = inputrows[0]
    for row in inputrows[1:]:
        newl = f'[{last_row},{row}]'
        #print(f"NEWL: {newl}")
        last_row = print_tree(calculate(build_tree(newl)))
        #print(f'* {last_row}')
    #print(last_row)


    print(f'Part 1: {get_magnitude(build_tree(last_row))}')

    max_mag = 0
    for i in range(len(inputrows)-1):
        for j in range(i, len(inputrows)):
            t1 = f'[{inputrows[i]},{inputrows[j]}]'
            max_mag = max(max_mag, get_magnitude(calculate(build_tree(t1))))
            t2 = f'[{inputrows[j]},{inputrows[i]}]'
            max_mag = max(max_mag, get_magnitude(calculate(build_tree(t2))))

    print(f'Part 2: {max_mag}')




    example = "[[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]"
    # example ="[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    # example = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
 #   root_node = build_tree(example)
 #   reconstructed = print_tree(root_node)

#    if example != reconstructed:
#        print(" - !!! -- Not equal -- !!! -")
#        print(example)
#        print(reconstructed)
#        print("-----------------------------")

    #    _, _, has_exploded = explode(root_node, 0)
    #    print(f'example: {example}')
    #    print(f'explode: {print_tree(root_node)}')
    #    print(has_exploded)
    #    return None

 #   new_result = print_tree(calculate(root_node))

#    print(f'example: {example}')
#    print(f'explode: {new_result}')

    return None

def calculate(root_node):
    no_change = False
    while not no_change:
        #print("no_change_loop")
        no_change = True
        has_exploded = True
        while has_exploded:
            _, _, has_exploded = explode(root_node, 0)
            if has_exploded:
       #         print(f'Explode: {print_tree(root_node)}')
                no_change = False
       #     else:
      #          print('no explode')

        has_split = split_node(root_node)
        if has_split:
     #       print(f'Split  : {print_tree(root_node)}')
            no_change = False
        #else:
    #        print("no explode")
    return root_node


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
