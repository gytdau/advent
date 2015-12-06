from inputData import *

lights = [[0 for i in range(1000)] for j in range(1000)]


# This just needed slight modification.


def process_light(instruction, x, y):
    type = instruction[0]
    if type == 1:
        lights[x][y] += 1
    elif type == 2:
        turn_off_light(x, y)
    else:
        lights[x][y] += 2


def turn_off_light(x, y):
    if lights[x][y] > 0:
        lights[x][y] -= 1


for instruction in instructions:
    # Squares!
    for x in range(instruction[1], instruction[3] + 1):
        for y in range(instruction[2], instruction[4] + 1):
            process_light(instruction, x, y)

print(sum(map(sum, lights)))
