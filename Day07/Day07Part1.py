beam_indexes = []
output_lines = []
splits = 0

with open("Day07/Input.txt", 'r') as file:
    lines = file.readlines()

for line in lines:
    working_line = list(line)
    for index in beam_indexes:
        if 0 <= index < len(working_line):
            if working_line[index] == '^':
                working_line[index-1] = '|'
                working_line[index+1] = '|'
                splits += 1
            else:
                working_line[index] = '|'
    updated_line = ''.join(working_line)
    output_lines.append(updated_line)
    beam_indexes = [ i for i, c in enumerate(updated_line) if c == 'S' or c == '|' ]

print(splits)
