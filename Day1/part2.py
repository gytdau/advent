from inputData import *


x = 0
counter = 0
for i in instructions:
    counter += 1
    if i == "(":
        x += 1
    else:
        x -= 1

    if x < 0:
        print(counter)
        break
