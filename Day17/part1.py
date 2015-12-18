import itertools

data = []

"""
Process inputData.txt and put it into the data array.
"""
with open("inputData.txt", "r") as infile:
    for line in infile:
        data.append(int(line))


valid_permutations = 0

def checkIfValid(permutation):
    return 1 if sum(permutation) == 150 else 0

"""
Main loop
 This is the best explanation I could come up with:
 1. For every possible amount of containers (e.g. if there are 4 containers, try 1, 2, 3, and 4)
 2. And for every possible combination of that amount of containers
"""
for i in range(0, len(data)):
    for permutation in itertools.combinations(data, i):
        valid_permutations += checkIfValid(permutation)

print("Answer: " + str(valid_permutations))
