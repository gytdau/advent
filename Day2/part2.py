from inputData import *

ribbon = 0
for i in range(0, len(data), 3):
    length = data[i]
    width = data[i+1]
    height = data[i+2]
    
    things = [length, width, height]
    things.remove(max(things))

    ribbon += (2 * things[0] + 2 * things[1])
    ribbon += length * width * height
print(ribbon)
