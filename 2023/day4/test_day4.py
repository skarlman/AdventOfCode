from collections import defaultdict, deque


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()
        score_part1 = 0

        copies = defaultdict(int)

        for line in lines:
            card_score = 0
            card_number, winners, mine = line.replace(':', '|').split('|')
            card_number = int(card_number.strip().split()[-1])
            w_split = winners.strip().replace('  ', ' ').split(' ')
            winners = [int(x.strip()) for x in w_split]
            m_split = mine.strip().replace('  ', ' ').split(' ')
            mine = [int(x.strip()) for x in m_split]

            new_copies = 0
            for num in mine:
                if num in winners:
                    new_copies += 1

                    if card_score > 0:
                        card_score *= 2
                    else:
                        card_score = 1

            if new_copies > 0:
                for c in range(1, new_copies+1):
                    copies[card_number + c] += (1 + copies[card_number])

            # print(card_score)
            score_part1 += card_score

    score_part2 = card_number
    for i in range(1, card_number+1):
        score_part2 += copies[i]

    return score_part1 if part == 1 else score_part2


# print(f'Part 1: {solve(1, True)}')
print(f'Part 2: {solve(2, False)}')
