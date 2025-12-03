from utils.api import get_input

inp = get_input(3)

total = 0

for line in inp.splitlines():
    numbers = list(map(int, list(line)))
    digit1 = max(numbers[:-1])
    digit2 = max(numbers[numbers.index(digit1) + 1 :])
    total += digit1 * 10 + digit2

print(total)
