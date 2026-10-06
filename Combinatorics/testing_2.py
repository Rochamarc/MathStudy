from main import generate_simple_hash
from random import choice

results = {}

# hashes de 1 a 10

for k in range(1, 11):
	
	hashes = []

	print("Running on Hash Key: {}".format(k))


	for i in range(36**k):
		key = generate_simple_hash(k)

		
		print(f"Key: {key}    Iterator: {i}    Hash length: {k}", end='\r')

		if key in hashes:
			results[f'{k}'] = i
			print(results)
			break

		hashes.append(key)

print(results)