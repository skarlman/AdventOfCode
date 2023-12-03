import math
from collections import defaultdict


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

        total_red = 12
        total_green = 13
        total_blue = 14

        score_part1 = 0
        score_part2 = 0

        for line in lines:
            line = line.strip()
            ss = line.split(':')
            ss2 = ss[0].split(' ')

            game_index = int(ss2[1])
            games = ss[1].split(';')

            max_colors = defaultdict(int)

            for game in games:
                game = game.strip()
                for dice in game.split(','):
                    dice = dice.strip()
                    color = dice.split(' ')[1]
                    amount = int(dice.split(' ')[0])
                    max_colors[color] = max(max_colors[color], amount)

            if max_colors['red'] <= total_red and max_colors['green'] <= total_green and max_colors[
                'blue'] <= total_blue:
                score_part1 += game_index

            score_part2 += math.prod(max_colors.values())

    return score_part1 if part == 1 else score_part2


print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
