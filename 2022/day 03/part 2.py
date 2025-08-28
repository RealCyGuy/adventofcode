from utils.api import get_input

inp = get_input(3)

total = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sets = []

for line in inp.splitlines():
    sets.append(set(line))
    if len(sets) == 3:
        shared = set.intersection(*sets)
        total += letters.index(shared.pop()) + 1
        sets = []

print(total)
