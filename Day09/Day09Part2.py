from itertools import combinations

largest_area = 0

def order_pair(a, b):
    return min(a, b), max(a, b)

def within_edges(x: int, y: int, vertical_edges, horizontal_edges) -> bool:
    for edge in horizontal_edges:
        (edge_start_x, edge_end_x), edge_y = edge
        if y == edge_y and edge_start_x <= x <= edge_end_x:
            return True
    
    for edge in vertical_edges:
        edge_x, (edge_start_y, edge_end_y) = edge
        if x == edge_x and edge_start_y <= y <= edge_end_y:
            return True
    
    crossings = 0

    for edge in vertical_edges:
        edge_x, (y1, y2) = edge
        edge_start_y, edge_end_y = order_pair(y1, y2)
        if edge_start_y <= y < edge_end_y:
            if edge_x > x:
                crossings += 1
    
    return (crossings % 2) == 1

def rect_boundary_inside(x_min, x_max, y_min, y_max, vertical_edges, horizontal_edges) -> bool:
    # Top and bottom edges: y = y_min and y = y_max
    for x in range(x_min, x_max + 1):
        print(f"Checking {x} in {x_max} ")
        if not within_edges(x, y_min, vertical_edges, horizontal_edges):
            return False
        if not within_edges(x, y_max, vertical_edges, horizontal_edges):
            return False

    # Left and right edges: x = x_min and x = x_max
    # (skip corners to avoid duplicate checks)
    for y in range(y_min + 1, y_max):
        print(f"Checking {y} in {y_max}")
        if not within_edges(x_min, y, vertical_edges, horizontal_edges):
            return False
        if not within_edges(x_max, y, vertical_edges, horizontal_edges):
            return False

    return True


# Generate coordinate list
print("Generating coordinate list...")
coordinates = []
with open("Day09/Input.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        x, y = line.split(',')
        coordinates.append((int(x),int(y)))

# Generate edges
print("Generate edges...")
horizontal_edges = []
vertical_edges = []
for iterator in range(len(coordinates)):
    edge_start = {"x": coordinates[iterator - 1][0],
                  "y": coordinates[iterator - 1][-1]}
    edge_end = {"x": coordinates[iterator][0],
                "y": coordinates[iterator][-1]}
    if edge_start["y"] == edge_end["y"]:
        y = edge_start["y"]
        x_range = (order_pair(edge_start["x"], edge_end["x"]))
        edge = (x_range, y)
        horizontal_edges.append(edge)
    elif edge_start["x"] == edge_end["x"]:
        x = edge_start["x"]
        y_range = (order_pair(edge_start["y"], edge_end["y"]))
        edge = (x, y_range)
        vertical_edges.append(edge)
    else:
        print(f"Edge not aligned: {edge_start} -> {edge_end}")

# Check all box combinations
for (a_x, a_y), (b_x, b_y) in combinations(coordinates, 2):
    print(f"Check box: ({a_x}, {a_y})->({b_x}, {b_y})")
    dist_x = abs(a_x - b_x) + 1
    dist_y = abs(a_y - b_y) + 1
    current_area = dist_x * dist_y

    if current_area < largest_area:
        continue

    x_min, x_max = order_pair(a_x, b_x)
    y_min, y_max = order_pair(a_y, b_y)

    if not within_edges(x_min, y_min, vertical_edges, horizontal_edges): continue
    if not within_edges(x_min, y_max, vertical_edges, horizontal_edges): continue
    if not within_edges(x_max, y_min, vertical_edges, horizontal_edges): continue
    if not within_edges(x_max, y_max, vertical_edges, horizontal_edges): continue
    
    invalid = False

    if not rect_boundary_inside(x_min, x_max, y_min, y_max, vertical_edges, horizontal_edges): continue
    
    largest_area = current_area

print(largest_area)
