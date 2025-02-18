from utils.api import get_input

inp = get_input(2)

rps1 = "ABC"
rps2 = "XYZ"

score = 0
for line in inp.splitlines():
    a, b = line.split()
    a = rps1.index(a)
    b = rps2.index(b)
    diff = (a - b) % 3
    if diff == 0:
        score += 3
    elif diff == 2:
        score += 6
    score += b + 1

print(score)
