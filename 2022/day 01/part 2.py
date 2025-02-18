from utils.api import get_input

inp = get_input(1)

all_calories = []
calories = 0
for line in inp.splitlines():
    if line:
        calories += int(line)
    else:
        all_calories.append(calories)
        calories = 0

print(sum(sorted(all_calories, reverse=True)[:3]))
