from utils.api import get_input

inp = get_input(5)
shortest = len(inp)
for unit in ["-"] + list(set(inp.lower())):
    if unit == "-":
        polymer = inp
    else:
        polymer = inp.replace(unit, "").replace(unit.upper(), "")
    react = True
    while react:
        react = False
        new = ""
        i = 0
        while i < len(polymer):
            char = polymer[i]
            if i == len(polymer) - 1:
                new += char
                break
            next_char = polymer[i + 1]
            if char != next_char and char.lower() == next_char.lower():
                react = True
                i += 1
            else:
                new += char
            i += 1
        polymer = new
    if unit == "-":
        inp = polymer
    if len(polymer) < shortest:
        shortest = len(polymer)
print(shortest)
