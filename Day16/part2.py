data = []

"""
I am assuming the desired quantities aren't generated randomly for each user.
"""
desired = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

""""
Process inputData.txt and puts it into the data array.
"""
with open("inputData.txt", "r") as infile:
    for line in infile:
        line = line.split()
        data.append(
                [
                    int(line[1][:-1]),
                    line[2][:-1], # First object
                    int(line[3][:-1]),
                    line[4][:-1], # Second object
                    int(line[5][:-1]),
                    line[6][:-1], # Third object
                    int(line[7])

                ]
        )


"""
Checks if this aunt has the correct amount of 'name'
This function was edited to conform to the new rules
"""
def checkIfValid(name, quantity):
    if name == "cats" or name == "trees":
        return desired[name] < quantity

    if name == "pomeranians" or name == "goldfish":
        return desired[name] > quantity

    return desired[name] == quantity


"""
Main loop - checks if each aunt has the correct amount.
"""
for aunt in data:
    if checkIfValid(aunt[1], aunt[2]) and checkIfValid(aunt[3], aunt[4]) and checkIfValid(aunt[5], aunt[6]):
        print("Aunt " + str(aunt[0]))


