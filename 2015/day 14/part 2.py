from utils.api import get_input

inp = get_input(14)

reindeer = []
for line in inp.splitlines():
    speed, fly, rest = [int(x) for x in line.split() if x.isnumeric()]
    reindeer.append(
        {"speed": speed, "fly": fly, "rest": rest, "points": 0, "distance": 0}
    )
max_distance = 0
for i in range(2503):
    for r in reindeer:
        if i % (r["fly"] + r["rest"]) < r["fly"]:
            r["distance"] += r["speed"]
        if r["distance"] > max_distance:
            max_distance = r["distance"]
    for r in reindeer:
        if r["distance"] == max_distance:
            r["points"] += 1
print(max(reindeer, key=lambda x: x["points"])["points"])
