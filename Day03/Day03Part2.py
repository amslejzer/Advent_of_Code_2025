total_joltage = 0

def best_k_subseq_stack(s: str, k: int = 12) -> str:
    drop = len(s) - k
    stack = []
    for ch in s:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return "".join(stack[:k])

with open("Day03/Input.txt", "r") as file:
    for line in file:
        bank = line.strip()
        bank_joltage = best_k_subseq_stack(bank, 12)
        total_joltage += int(bank_joltage)

print(total_joltage)
                