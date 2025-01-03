from utils.api import get_input

inp = get_input(1)
list1 = []
list2 = []
for line in inp.splitlines():
    split = line.split()
    list1.append(int(split[0]))
    list2.append(int(split[1]))
list1.sort()
list2.sort()
similarity = 0
for x, y in zip(list1, list2):
    similarity += x * list2.count(x)
print(similarity)
