from collections import defaultdict

from utils.api import get_input

inp = get_input(7)

wd = []
directories = defaultdict(int)
for line in inp.splitlines():
    if line.startswith("$ cd "):
        cd = line[5:]
        if cd == "..":
            wd.pop()
        else:
            wd.append(cd)
    elif not line.startswith("$"):
        size, name = line.split(" ")
        if size.isdecimal():
            size = int(size)
            wd_key = tuple(wd)
            directories[wd_key] += size
            for i in range(1, len(wd_key)):
                directories[wd_key[:-i]] += size

need_to_free = directories[("/",)] - 40000000
smallest = 0
for size in directories.values():
    if size > need_to_free and (smallest == 0 or size < smallest):
        smallest = size

print(smallest)
