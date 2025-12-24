import re

lines = []
grand_total = 0
tup_ruler = []
new_lines = []


with open("Day06/Input.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]

ruler = re.split(r" (?=\S)", lines[-1])
lines.pop()
temp = 0
for col in ruler:
    tup_ruler.append((temp, len(col)))
    temp += len(col) + 1

for line in lines:
    new_line = []
    for col in tup_ruler:
        new_line.append(line[col[0]:(col[0]+col[1])])
    new_lines.append(new_line)

for *values, operation in reversed(list(zip(*new_lines, ruler))):
    new_values = []
    result = 0
    for iterator in range(1, len(operation)+1):
        current_value = ''
        for value in values:
            current_value = current_value + value[-iterator]
        new_values.append(current_value)
    if operation.strip() == '+':
        for value in new_values:
            result += int(value)
    elif operation.strip() == '*':
        result = int(new_values[0])
        for value in new_values[1:]:
            result *= int(value)
    grand_total += result

print(grand_total)