import re

from utils.api import get_input

inp = get_input(5)

stacks: list[list[int]] = []
instructions = False

for line in inp.splitlines():
    if not instructions:
        for i, char in enumerate(line):
            if (i - 1) % 4 == 0:
                s = (i - 1) // 4
                if len(stacks) <= s:
                    stacks.append([])
                if char.isalpha():
                    stacks[s].append(char)
    else:
        a, b, c = map(int, re.findall(r"\d+", line))
        b -= 1
        c -= 1
        for _ in range(a):
            stacks[c].insert(0, stacks[b].pop(0))
    if not line:
        instructions = True

word = ""
for s in stacks:
    word += s[0]

print(word)
