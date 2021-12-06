gamma = 0
epsilon = 0

total = 0

ctr = None

oxygenList = []
co2List = []

while True:
    try:
        line = input()

        oxygenList.append(line)
        co2List.append(line)

        if ctr == None:
            ctr = [0] * len(line)

        total += 1

        for i in range(len(line)):
            if line[i] == '1':
                ctr[i] += 1


    except EOFError:
        break
# 10111

gammaList = ['1' if x >= total / 2 else '0' for x in ctr]
gamma = int("".join(gammaList), 2)

epsilonList = ['0' if x >= total / 2 else '1' for x in ctr]
epsilon = int("".join(epsilonList), 2)

print(f'1: {gamma * epsilon} (198) (3148794)')

bits = len(oxygenList[0])
for bitNo in range(bits):
    keep = []
    m = list(map(lambda x: int(x[bitNo]), oxygenList))
    isOne = "1" if sum(m) >= (len(oxygenList) / 2) else "0"

    for o in oxygenList:
        if o[bitNo] == isOne:
            keep.append(o)
    oxygenList = keep
    if len(keep) == 1:
        break

oxygen = int("".join(oxygenList[0]), 2)
print(oxygen)


for bitNo in range(bits):
    keep = []
    m = list(map(lambda x: int(x[bitNo]), co2List))
    isOne = "0" if sum(m) >= (len(co2List) / 2) else "1"

    for o in co2List:
        if o[bitNo] == isOne:
            keep.append(o)
    co2List = keep
    if len(keep) == 1:
        break


co2 = int("".join(co2List[0]), 2)
print(co2)

print(f'2: {oxygen * co2}')
