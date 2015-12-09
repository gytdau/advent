data = []

with open("inputData.txt", "r") as infile:
    for line in infile:
        line = line.replace('x', ' ')
        data += line.split()


paper = 0
for i in range(0, len(data), 3):
    length = int(data[i])
    width = int(data[i+1])
    height = int(data[i+2])

    paper += (2 * length * width) + (2 * width * height) + (2 * height * length)
    paper += min((length * width), (width * height), (height * length))

print(paper)
