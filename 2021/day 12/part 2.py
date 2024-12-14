from collections import defaultdict, deque

from utils.api import get_input

inp = get_input(12)

graph = defaultdict(list)
for line in inp.splitlines():
    split = line.split("-")
    graph[split[0]].append(split[1])
    graph[split[1]].append(split[0])

queue = deque([("start", set(), None)])
paths = 0

while queue:
    node, visited, twice = queue.popleft()
    if node == "end":
        paths += 1
        continue
    visited = visited.copy()
    if node.islower():
        visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append((neighbour, visited, twice))
        elif twice is None and neighbour != "start":
            queue.append((neighbour, visited, node))

print(paths)
