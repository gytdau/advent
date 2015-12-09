data = []

with open("inputData.txt", "r") as infile:
    for line in infile:
        line = line.replace('x', ' ')
        data += line.split()

ribbon = 0
for i in range(0, len(data), 3):
    length = int(data[i])
    width = int(data[i+1])
    height = int(data[i+2])
    
    things = [length, width, height]
    things.remove(max(things))

    ribbon += (2 * things[0] + 2 * things[1])
    ribbon += length * width * height
print(ribbon)
