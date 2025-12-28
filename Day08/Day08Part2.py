from itertools import combinations
from collections import defaultdict
import math
from math import prod

junction_boxes = {}
connections = {}
circuits = defaultdict(list)
connection_log = []

with open("Day08/Input.txt", 'r') as file:
    for iterator, line in enumerate(file):
        line = line.rstrip('\n')
        junction_box = { "x": int(line.split(',')[0]), "y": int(line.split(',')[1]), "z": int(line.split(',')[2])}
        junction_boxes[iterator] = junction_box

for (a_id, a_values), (b_id, b_values) in combinations(junction_boxes.items(), 2):
    new_key = str(a_id) + '_' + str(b_id)
    x_distance_sqd = pow(a_values['x'] - b_values['x'], 2)
    y_distance_sqd = pow(a_values['y'] - b_values['y'], 2)
    z_distance_sqd = pow(a_values['z'] - b_values['z'], 2)
    sl_distance = math.sqrt(x_distance_sqd + y_distance_sqd + z_distance_sqd)
    connections[new_key] = sl_distance

sorted_connections = sorted(connections.items(), key=lambda item: item[1])

for iterator, item in enumerate(sorted_connections):
    a_id = item[0].split('_')[0]
    b_id = item[0].split('_')[-1]
    a_circuit = None
    b_circuit = None
    for circuit, boxes in circuits.items():
        if a_id in boxes:
            a_circuit = circuit
        if b_id in boxes:
            b_circuit = circuit
    if a_circuit != None and b_circuit == None:
        circuits[a_circuit].append(b_id)
        connection_log.append(item[0])
    elif b_circuit != None and a_circuit == None:
        circuits[b_circuit].append(a_id)
        connection_log.append(item[0])
    elif a_circuit != None and b_circuit != None and a_circuit != b_circuit:
        circuits[a_circuit].extend(circuits[b_circuit])
        circuits.pop(b_circuit, None)
        connection_log.append(item[0])
    elif a_circuit == None and b_circuit == None:
        circuits[iterator].extend([a_id, b_id])
        connection_log.append(item[0])

last_connection = connection_log[-1].split('_')
last_x_coordinates = []
for id in last_connection:
    last_x_coordinates.append(junction_boxes[int(id)]['x'])
    
print(prod(last_x_coordinates))