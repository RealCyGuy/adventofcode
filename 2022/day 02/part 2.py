from utils.api import get_input

inp = get_input(2)

rps1 = "ABC"
rps2 = "XYZ"
results = [-1, 0, 1]

score = 0
for line in inp.splitlines():
    a, b = line.split()
    a = rps1.index(a)
    b = rps2.index(b)
    if b == 1:
        score += 3
    elif b == 2:
        score += 6
    score += ((a + results[b]) % 3) + 1

print(score)
