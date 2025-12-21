total_joltage = 0

with open("Day03/Input.txt", "r") as file:
    for line in file:
        bank = line.strip()
        bank_joltage = 0
        for outer_iterator in range(0, len(bank)-1):
            for inner_iterator in range(outer_iterator+1, len(bank)):
                combo_joltage = int(bank[outer_iterator] + bank[inner_iterator])
                if combo_joltage > bank_joltage:
                    bank_joltage = combo_joltage
        total_joltage += bank_joltage

print(total_joltage)
                