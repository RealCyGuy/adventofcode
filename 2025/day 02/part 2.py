from utils.api import get_input

inp = get_input(2)

total = 0
for pair in inp.split(","):
    a, b = map(int, pair.split("-"))
    for n in range(a, b + 1):
        n_str = str(n)
        for i in range(1, len(n_str)):
            if len(n_str) % i == 0:
                j = i
                while j < len(n_str):
                    if n_str[j : j + i] != n_str[0:i]:
                        break
                    j += i
                if j >= len(n_str):
                    total += n
                    break

print(total)
