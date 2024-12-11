from utils.api import get_input

inp = get_input(11)
grid = []
for line in inp.splitlines():
    if line.count("#") == 0:
        grid.append(line)
    grid.append(line)
expansions = []
for x in range(len(grid[0])):
    galaxy = False
    for line in grid:
        if line[x] == "#":
            galaxy = True
            break
    if not galaxy:
        expansions.append(x)
new_grid = []
for line in grid:
    line = list(line)
    for x in reversed(expansions):
        line.insert(x, ".")
    line = "".join(line)
    new_grid.append(line)
grid = new_grid
total = 0
galaxies = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            galaxies.append((x, y))
for i, galaxy in enumerate(galaxies[:-1]):
    for pair in galaxies[i + 1 :]:
        total += abs(galaxy[0] - pair[0]) + abs(galaxy[1] - pair[1])
print(total)
