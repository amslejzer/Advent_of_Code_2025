position = 50
ZeroCount = 0

with open("Day01/Input.txt") as Input:
    for line in Input:
        direction = line[0]
        steps = int(line[1:])
        for i in range(steps):
            if direction == "R":
                position = (position + 1) % 100
            elif direction == "L":
                position = (position - 1) % 100
            if position == 0:
                ZeroCount += 1

print(ZeroCount)