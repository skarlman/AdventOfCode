from collections import defaultdict, deque
import re


def fixline(line):
    letter_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six":6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}



    new_line =line
    found = False

    for i in range(len(line)):

        for word in letter_dict.keys():
            if word in line[:i]:
                new_line = line[:i].replace(word, str(letter_dict[word])) + line[i:]
                found = True
                break
        if found:
            break

        if line[i].isdigit():
            break

    found = False
    for i in range(len(new_line)):
        j = i+1
        if new_line[-j].isdigit():
            break
        for word in letter_dict.keys():
            if word in new_line[-j:]:
                new_line = new_line[:-j] + new_line[-j:].replace(word, str(letter_dict[word]))
                found = True
                break
        if found:
            break

    print(f'{line.strip()}')
    print(f'{new_line}')
    return new_line


    # return line.replace("two", "2").replace("one", "1").replace("eight", "8").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("nine", "9").replace("zero", "0")



def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()
        score_part1 = 0
        for line in lines:
            real_line = fixline(line) if part == 2 else line
            reversed_line = real_line[::-1]

            # print(real_line)
            f = real_line[re.search(r"\d", real_line).start()]
            l = reversed_line[re.search(r"\d", reversed_line).start()]
            new_digit = int(f'{f}{l}')
            print(f'{new_digit}')
            score_part1 += new_digit



    return score_part1




print(f'Part 1: {solve(2, False)}')
# print(f'Part 2: {solve(2, False)}')

