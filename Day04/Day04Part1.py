DIRECTIONS_8 = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def count_neighbors(grid, pos_x: int, pos_y: int, target):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for row_offset, col_offset in DIRECTIONS_8:
        neighbor_row, neighbor_col = pos_x + row_offset, pos_y + col_offset
        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
            if grid[neighbor_row][neighbor_col] == target:
                count += 1
    
    return count

accessible_count = 0

with open("Day04/Input.txt") as input_file:
    input_grid = [list(line.strip()) for line in input_file]

for row_index in range(len(input_grid)):
    for col_index in range(len(input_grid[0])):
        if(input_grid[row_index][col_index] == '@'):
            count = count_neighbors(input_grid, row_index, col_index, '@')
            if count < 4:
                accessible_count += 1

print(accessible_count)