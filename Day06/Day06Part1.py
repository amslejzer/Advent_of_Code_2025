lines = []
grand_total = 0

with open("Day06/TestInput.txt", "r") as file:
    for line in file:
        lines.append(line.split())

for items in zip(*lines):
    column_result = 0
    operation = items[-1]
    if operation == '+':
        for iterator in range(len(items) - 1):
            column_result += int(items[iterator])
    elif operation == '*':
        column_result = int(items[0])
        for iterator in range(1, len(items) - 1):
            column_result *= int(items[iterator])
    grand_total += column_result

print