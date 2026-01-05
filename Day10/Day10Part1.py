from itertools import combinations

total_button_prtesses = 0

def decode_binary_string(text_lights: str, zero: str, one: str) -> int:
    if not text_lights:
        raise ValueError("Input string is empty.")
    if zero == one:
        raise ValueError("Characters for zero and one must be different.")
    
    n = 0
    for char in text_lights:
        if char == zero:
            bit = 0
        elif char == one:
            bit = 1
        else:
            raise ValueError(f"Invalid character {char!r}; expected {zero!r} or {one!r}")
        n = (n << 1 ) | bit
    return n

with open("Day10/Input.txt", 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        text_lights = line.split(' ')[0].strip("[]")
        binary_lights = decode_binary_string(text_lights, '.', '#')
        text_buttons = line.split(' ')[1:-1]
        binary_buttons = []
        for text_button in text_buttons:
            bits_positions = [int(x) for x in text_button.strip("()").split(',')]
            bits = []
            for iterator in range(len(text_lights)):
                if iterator in bits_positions:
                    bits.append('1')
                else:
                    bits.append('0')
            bit_string = ''.join(bits)
            button = decode_binary_string(bit_string, '0', '1')
            binary_buttons.append(button)
        
        print(binary_buttons)

        found = 0
        min_buttons = 0
        for iterator in range(1, len(binary_buttons)+1):
            print(f"Iterator: {iterator}")
            for combo in combinations(binary_buttons, iterator):
                print(f"Combo: {combo}")
                n = 0
                for mask in combo:
                    print(f"n = n ^ {bin(mask)}")
                    n = n ^ mask
                    print(f"working n: {n}")
                print(f"final n: {bin(n)}")
                if n == binary_lights:
                    found = iterator
                    break
            if found != 0:
                min_buttons = iterator
                break
        total_button_prtesses += min_buttons

print(total_button_prtesses)