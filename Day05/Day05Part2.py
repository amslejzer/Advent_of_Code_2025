file_path = "Day05/Input.txt"

with open(file_path, "r") as input_file:
    content = input_file.read().strip()

id_ranges, available_ids = content.split("\n\n", maxsplit=1)
id_ranges = id_ranges.splitlines()
available_ids = available_ids.splitlines()
fresh_ingredients = 0
fresh_ids = 0

sorted_id_ranges = sorted(
    id_ranges,
    key=lambda line: int(line.split('-')[0])
)

non_overlapping_ranges = [sorted_id_ranges[0]]

for iterator in range(len(sorted_id_ranges)):
    if iterator >= 1:
        current_range = sorted_id_ranges[iterator]
        current_floor = int(current_range.split('-')[0])
        current_ceiling = int(current_range.split('-')[-1])
        previous_range = non_overlapping_ranges[-1]
        previous_floor = int(previous_range.split("-")[0])
        previous_ceiling = int(previous_range.split('-')[-1])
        if current_floor <= previous_ceiling:
            new_range = non_overlapping_ranges[-1].split('-')[0] + '-' + str(max(current_ceiling, previous_ceiling))
            non_overlapping_ranges[-1] = new_range
        else:
            non_overlapping_ranges.append(current_range)

for range in non_overlapping_ranges:
    fresh_ids += int(range.split('-')[-1]) - int(range.split('-')[0]) + 1

print(fresh_ids)