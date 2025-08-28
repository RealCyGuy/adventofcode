from utils.api import get_input

inp = get_input(3)

total = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for line in inp.splitlines():
    l = len(line)
    shared = set(line[: l // 2]) & set(line[l // 2 :])
    total += letters.index(shared.pop()) + 1

print(total)
