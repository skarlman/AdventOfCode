
aim = 0

x=0
d=0

while True:
    try :
        line = input().split()

        if line[0] == "forward":
            x+=int(line[1])
            d += aim*int(line[1])
        elif line[0] == "up":
            aim -= int(line[1])
        elif line[0] == "down":
            aim += int(line[1])

    except EOFError:
        break





print(x*d)