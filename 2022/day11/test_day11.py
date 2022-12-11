import math
import operator
from collections import defaultdict, deque
from math import floor


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        lines = [r.strip() for r in openfileobject.readlines()]

    monkey_items = []
    monkey_operation = []
    monkey_test = []
    monkey_inspections = []
    monkey_divisors = []

    for i in range(0, len(lines), 7):
        # monkey_number = i // 7
        monkey_inspections.append(0)
        monkey_items.append([int(x) for x in lines[i + 1].split(':')[1].split(',')])

        op_val = lines[i + 2].split(' ')[-1]

        if '*' in lines[i + 2]:
            monkey_operation.append(
                (lambda x, op_val=op_val: operator.mul(x, int(op_val) if op_val.isnumeric() else x)))
        else:
            monkey_operation.append(
                (lambda y, op_val=op_val: operator.add(y, int(op_val) if op_val.isnumeric() else y)))
        # print(monkey_operation[-1](2))

        divisor = int(lines[i + 3].split(' ')[-1])
        true_monkey = int(lines[i + 4].split(' ')[-1])
        false_monkey = int(lines[i + 5].split(' ')[-1])
        monkey_divisors.append(divisor)
        monkey_test.append((lambda x, divisor=divisor, true_monkey=true_monkey,
                                   false_monkey=false_monkey: true_monkey if x % divisor == 0 else false_monkey))

    # for i in range(len(monkey_operation)):
    #     print(f'{i}: {monkey_operation[i](2)}')
    #
    # exit(0)

    total_monkeys = len(monkey_items)
    for round_number in range(20 if part == 1 else 10000):
        # print(round_number)
        for monkey_number in range(total_monkeys):
            while monkey_items[monkey_number]:
                monkey_inspections[monkey_number] += 1
                item = monkey_items[monkey_number].pop(0)
                worry = monkey_operation[monkey_number](item)
                if part == 1:
                    worry = floor(worry / 3)
                # print(worry)
                new_monkey = monkey_test[monkey_number](worry)

                # modded_worry = monkey_operation[new_monkey](worry) % (monkey_divisors[new_monkey])
                modded_worry = worry
                monkey_items[new_monkey].append(modded_worry)

        # print()
        # print(f"round {round_number}")
        # for r in monkey_items:
        #     print(r)

    sorted_handles = sorted(monkey_inspections, reverse=True)[:2]
    monkey_business = math.prod(sorted_handles)
    return monkey_business


print(f'Part 1 [10605]: {solve(1, True)}')
print(f'Part 2: {solve(2, False)}')
