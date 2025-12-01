from utils.api import get_input

inp = get_input(1)

dial = 50
count = 0

for line in inp.splitlines():
    if line.startswith("R"):
        dial += int(line[1:])
    else:
        dial -= int(line[1:])
    dial %= 100
    if dial == 0:
        count += 1

print(count)
