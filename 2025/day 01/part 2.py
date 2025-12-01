from utils.api import get_input

inp = get_input(1)

dial = 50
count = 0

for line in inp.splitlines():
    previous_dial = dial
    if line.startswith("R"):
        dial += int(line[1:])
    else:
        dial -= int(line[1:])
        # why do these work
        if previous_dial == 0:
            count -= 1
        if dial % 100 == 0:
            count += 1
    c, dial = divmod(dial, 100)
    count += abs(c)

print(count)
