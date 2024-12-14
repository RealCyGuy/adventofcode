from utils.api import get_input

inp = get_input(5)
react = True
while react:
    react = False
    new = ""
    i = 0
    while i < len(inp):
        char = inp[i]
        if i == len(inp) - 1:
            new += char
            break
        next_char = inp[i + 1]
        if char != next_char and char.lower() == next_char.lower():
            react = True
            i += 1
        else:
            new += char
        i += 1
    inp = new
print(len(inp))
