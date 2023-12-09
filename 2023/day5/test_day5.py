from collections import defaultdict, deque


def solve(part, use_example):
    filename = "exampleinput.txt" if use_example else "input.txt"

    score_part1 = 0
    with open(filename) as openfileobject:
        # raw = openfileobject.read()
        lines = openfileobject.readlines()

        seeds = [int(x) for x in lines[0].split()[1:]]
        p2_seeds = []
        if part == 2:

            for s in range(0, len(seeds), 2):
                for si in range(seeds[s], seeds[s + 1]+seeds[s]):
                    p2_seeds.append(si)
        seeds = p2_seeds

        seed_to_soil = {}
        soil_to_fertilizer = {}
        fertilizer_to_water = {}
        water_to_light = {}
        light_to_temperature = {}
        temperature_to_humidity = {}
        humidity_to_location = {}
        all_dicts = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                     temperature_to_humidity, humidity_to_location]

        dict_num = 0
        for line in lines[3:]:
            if line == '\n':
                dict_num += 1
                # print("dict_num", dict_num)
                continue
            if not line.split()[0].isdigit():
                continue

            mapping = [int(x) for x in line.strip().split()]
            all_dicts[dict_num][mapping[1]] = (mapping[2], mapping[0])
            # print(f'{mapping[1]} => ({mapping[2]} {mapping[0]})')

    lowest_location = 9 ** 10

    for seed in seeds:
        curr_seed_val = seed
        found_conversion = False
        for di in range(len(all_dicts)):
            for k, v in all_dicts[di].items():
                if k <= curr_seed_val <= k + v[0]:
                    curr_seed_val = curr_seed_val - k + v[1]
                    found_conversion = True
                    break
            if found_conversion:
                continue

        lowest_location = min(curr_seed_val, lowest_location)

    return lowest_location



# print(f'Part 1: {solve(1, False)}')
print(f'Part 2: {solve(2, False)}')
