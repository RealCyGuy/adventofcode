from utils.api import get_input

inp = get_input(6)

current = []
for i, char in enumerate(inp):
    current.append(char)
    if len(current) > 4:
        current.pop(0)
        if len(set(current)) == 4:
            print(i + 1)
            break
