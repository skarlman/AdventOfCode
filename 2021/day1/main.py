

curr = []

curr.append(int(input()))
curr.append(int(input()))
curr.append(int(input()))

old = sum(curr)
incs = 0

while True:
    try :
        line = int(input())
        v = old - curr.pop(0) + line
        curr.append(line)

        if v > old:
            incs += 1

        old = v

    except EOFError:
        break





print(incs)