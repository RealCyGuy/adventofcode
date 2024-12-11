from utils.api import get_input

inp = get_input(13)
lines = inp.splitlines() + [""]

rows = []
columns = []

total = 0
for line in lines:
    if not line:
        vertical = False
        for i in range(1, len(columns)):
            match = True
            for front, back in zip(reversed(columns[:i]), columns[i:]):
                if front != back:
                    match = False
                    break
            if match:
                vertical = True
                total += i
                break
        if not vertical:
            for i in range(1, len(rows)):
                match = True
                for front, back in zip(reversed(rows[:i]), rows[i:]):
                    if front != back:
                        match = False
                if match:
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
