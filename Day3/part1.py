from inputData import *

posX = 0
posY = 0
locations = [(0, 0)]

ticker = False

for i in instructions:
    y = 0
    x = 0
    if i == "^":
        posY += 1
    elif i == "v":
        posY += -1
    elif i == "<":
        posX += 1
    elif i == ">":
        posX += -1
   
    location = (posX, posY)
    if location not in locations:
        locations.append(location)

       
print(len(locations))