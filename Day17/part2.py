import itertools

data = []

"""
Process inputData.txt and put it into the data array.
"""
with open("inputData.txt", "r") as infile:
    for line in infile:
        data.append(int(line))


valid_permutations = {}

def checkIfValid(permutation):
    return sum(permutation) == 150

"""
Main loop
 This is the best explanation I could come up with:
 1. For every possible amount of containers (e.g. if there are 4 containers, try 1, 2, 3, and 4)
 2. And for every possible combination of that amount of containers
"""
for i in range(0, len(data)):
    for permutation in itertools.combinations(data, i):
        if checkIfValid(permutation):
            """
            This was the logic that was modified.
            """
            if len(permutation) not in valid_permutations:
                valid_permutations[len(permutation)] = 1
            else:
                valid_permutations[len(permutation)] += 1

print("Answer: " + str(valid_permutations[min(valid_permutations)]))
