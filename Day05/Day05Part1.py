file_path = "Day05/Input.txt"

with open(file_path, "r") as input_file:
    content = input_file.read().strip()

id_ranges, available_ids = content.split("\n\n", maxsplit=1)
id_ranges = id_ranges.splitlines()
available_ids = available_ids.splitlines()
fresh_ingredients = 0

for id in available_ids:
    for id_range in id_ranges:
        floor = int(id_range.split('-')[0])
        ceiling = int(id_range.split('-')[-1])
        if floor <= int(id) <= ceiling:
            fresh_ingredients += 1
            break

print(fresh_ingredients)