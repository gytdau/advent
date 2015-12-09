from itertools import permutations

destinations = set()
distances = dict()

with open("inputData.txt", "r") as infile:
    for line in infile:
        values = line.split()
        # 0 = Departing, 2 = Arriving, 4 = Cost
        destinations.add(values[0])
        destinations.add(values[2])
        # This will create a dictionary of dictionaries of possible distances, e.g.
        # {'Tristram': {'AlphaCentauri': 34, 'Snowdin': 100}, (...)}
        distances.setdefault(values[0], dict())[values[2]] = int(values[4])
        distances.setdefault(values[2], dict())[values[0]] = int(values[4])


possible_distances = []

def getDistance(x, y):
    return distances[x][y]

for items in permutations(destinations):
    distancesT = map(getDistance, items[:-1], items[1:])
    total_fuel_used = sum(distancesT)
    possible_distances.append(total_fuel_used)

# This required very little modification.

longest_distance = max(possible_distances)
print(longest_distance)