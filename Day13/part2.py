from itertools import permutations


instructions = []
people = set()

with open("inputData.txt", "r") as infile:
    for line in infile:
        line = line.split()
        happiness = int(line[3])
        positive = line[2] == "gain"
        if not positive:
            happiness = -happiness

        instructions.append([line[0], line[10][:-1], happiness])

        people.add(line[0])
        people.add(line[10][:-1])


# ====== Include yourself
for person in people:
    instructions.append(["You", person, 0])
    instructions.append([person, "You", 0])

people.add("You")
# ====== End of changes

def get_happiness(a, b):
    # Search to match person `a`
    search_1 = [something for something in instructions if something[0] == a]

    # Search what we've found to match person `b`
    search_2 = [something for something in search_1 if something[1] == b]

    return search_2[0][2]


max_happiness = 0

for permutation in permutations(people):
    this_happiness = 0
    last_element = len(permutation) - 1
    for i, v in enumerate(permutation):
        # If this is the first element - because it's a round table, it's sitting beside the last element.
        if i == 0:
            this_happiness += get_happiness(v, permutation[last_element])
        else:
            this_happiness += get_happiness(v, permutation[i - 1])

        # Likewise for the last element - it's sitting beside the first element.
        if i == last_element:
            this_happiness += get_happiness(v, permutation[0])
        else:
            this_happiness += get_happiness(v, permutation[i + 1])

    max_happiness = max(this_happiness, max_happiness)

print(max_happiness)