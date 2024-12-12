from utils.api import get_input

inp = get_input(14)

distances = []
time = 2503
for line in inp.splitlines():
    speed, fly, rest = [int(x) for x in line.split() if x.isnumeric()]
    flying, leftover = divmod(time, fly + rest)
    distance = speed * flying * fly
    distance += speed * min(leftover, fly)
    distances.append(distance)
print(max(distances))
