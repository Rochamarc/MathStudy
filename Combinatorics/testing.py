from main import generate_simple_hash
from time import sleep

# Generating a simple Hash with 4 char the number of possibilities is equal to 37¹⁴ => 1874161
# Lets generate a this hash and run this number of times to see when we hit two equal hashes

hashes = []

for i in range(37**14):
    key = generate_simple_hash(4)
    print(key)

    sleep(0.1)

    if key in hashes:
        print("YUPIIIIII")
        print(f"We have a match at {i}")
        break

    hashes.append(key)

