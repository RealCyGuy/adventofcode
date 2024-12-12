import hashlib

from utils.api import get_input

inp = get_input(4)

i = 0
while True:
    _hash = hashlib.md5(f"{inp}{i}".encode()).hexdigest()
    if _hash.startswith("0" * 6):
        break
    i += 1
print(i)
