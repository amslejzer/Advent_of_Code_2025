from itertools import combinations
import math

coordinates = []
largest_area = 0

with open("Day09/Input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        x, y = line.split(',')
        coordinates.append((int(x),int(y)))

for (a_x, a_y), (b_x, b_y) in combinations(coordinates, 2):
    dist_x = abs(a_x - b_x) + 1
    dist_y = abs(a_y - b_y) + 1
    current_area = dist_x * dist_y
    if current_area > largest_area:
        largest_area = current_area

print(largest_area)