from collections import defaultdict

from utils.api import get_input

inp = get_input(6)

counts = defaultdict(int)

for lanternfish in inp.split(","):
    counts[int(lanternfish)] += 1

for _ in range(256):
    new_counts = defaultdict(int)
    for lanternfish, count in counts.items():
        if lanternfish == 0:
            new_counts[6] += count
            new_counts[8] += count
        else:
            new_counts[lanternfish - 1] += count
    counts = new_counts

print(sum(counts.values()))
