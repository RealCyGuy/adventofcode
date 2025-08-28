from utils.api import get_input

inp = get_input(4)

pairs = 0

for line in inp.splitlines():
    a, b = line.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    if (a1 >= b1 and a1 <= b2) or (a1 <= b1 and a2 >= b1):
        pairs += 1

print(pairs)
