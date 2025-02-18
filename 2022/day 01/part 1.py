from utils.api import get_input

inp = get_input(1)

max_calories = 0
calories = 0
for line in inp.splitlines():
    if line:
        calories += int(line)
    else:
        max_calories = max(max_calories, calories)
        calories = 0

print(max_calories)
