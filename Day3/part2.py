santaX = 0
santaY = 0
robotX = 0
robotY = 0
locations = [(0, 0)]

ticker = False

instructions = ""

with open("inputData.txt", "r") as infile:
    for line in infile:
        instructions += line
        
for i in instructions:
    y = 0
    x = 0
    if i == "^":
        y = 1
    elif i == "v":
        y = -1
    elif i == "<":
        x = 1
    elif i == ">":
        x = -1

    if ticker:
        ticker = False
        santaX += x
        santaY += y

        location = (santaX, santaY)
        if location not in locations:
            locations.append(location)
    else:
        ticker = True
        robotX += x
        robotY += y

        location = (robotX, robotY)
        if location not in locations:
            locations.append(location)

print(len(locations))
