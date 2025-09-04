from utils.api import get_input

inp = get_input(6)

current = []
for i, char in enumerate(inp):
    current.append(char)
    if len(current) > 14:
        current.pop(0)
        if len(set(current)) == 14:
            print(i + 1)
            break
