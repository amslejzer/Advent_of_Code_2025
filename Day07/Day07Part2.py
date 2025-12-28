from collections import defaultdict

beam_indexes = defaultdict(int)
next_indexes = defaultdict(int)
splits = 0
timelines = 0

with open("Day07/Input.txt", 'r') as file:
    lines = [line.rstrip("\n") for line in file]

for line in lines:
    for index, character in enumerate(line):
        if index in list(beam_indexes.keys()):
            if character == '^':
                splits += 1
                next_indexes[index-1] += beam_indexes[index]
                next_indexes[index+1] += beam_indexes[index]
            else:
                next_indexes[index] += beam_indexes[index]
        elif character == 'S':
            next_indexes[index] = 1
    beam_indexes = defaultdict(int, next_indexes)
    next_indexes.clear()
print(splits)
for i in beam_indexes.values():
    timelines += i
print(sum(beam_indexes.values()))