from utils.api import get_input

inp = get_input(2)

total = 0
for pair in inp.split(","):
    a, b = map(int, pair.split("-"))
    for n in range(a, b + 1):
        n_str = str(n)
        if len(n_str) % 2 == 0:
            if n_str[: len(n_str) // 2] == n_str[len(n_str) // 2 :]:
                total += n

print(total)
