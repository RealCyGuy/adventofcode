from utils.api import get_input

inp = get_input(13)
lines = inp.splitlines() + [""]

rows = []
columns = []


def count_differences(s1, s2):
    c = 0
    for a, b in zip(s1, s2):
        if a != b:
            c += 1
    return c


total = 0
for line in lines:
    if not line:
        vertical = False
        for i in range(1, len(columns)):
            differences = 0
            for front, back in zip(reversed(columns[:i]), columns[i:]):
                differences += count_differences(front, back)
            if differences == 1:
                vertical = True
                total += i
                break
        if not vertical:
            for i in range(1, len(rows)):
                differences = 0
                for front, back in zip(reversed(rows[:i]), rows[i:]):
                    differences += count_differences(front, back)
                if differences == 1:
                    total += i * 100
                    break
        rows = []
        columns = []
        continue
    rows.append(line)
    for i, char in enumerate(line):
        if i + 1 > len(columns):
            columns.append(char)
        else:
            columns[i] += char
print(total)