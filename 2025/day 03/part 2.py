from utils.api import get_input

inp = get_input(3)

total = 0

for line in inp.splitlines():
    numbers = list(map(int, list(line)))
    prev_index = -1
    for i in range(11, -1, -1):
        if i == 0:
            digit = max(numbers[prev_index + 1 :])
        else:
            digit = max(numbers[prev_index + 1 : -i])
        cur_index = numbers[prev_index + 1 :].index(digit) + prev_index + 1
        prev_index = cur_index
        total += digit * (10 ** (i))

print(total)
