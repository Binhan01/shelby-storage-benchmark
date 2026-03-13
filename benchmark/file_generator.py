import os
import random

folder = "test_files"
os.makedirs(folder, exist_ok=True)

sizes = [1, 5, 10, 20]

for i in range(20):
    size = random.choice(sizes)
    filename = f"{folder}/file_{i}_{size}MB.bin"

    with open(filename, "wb") as f:
        f.write(os.urandom(size * 1024 * 1024))

print("Files generated")