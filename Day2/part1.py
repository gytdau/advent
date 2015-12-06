from inputData import *

paper = 0
for i in range(0, len(data), 3):
    length = data[i]
    width = data[i+1]
    height = data[i+2]

    paper += (2 * length * width) + (2 * width * height) + (2 * height * length)
    paper += min((length * width), (width * height), (height * length))

print(paper)
