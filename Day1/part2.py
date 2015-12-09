
x = 0
counter = 0
characters = ""

with open("inputData.txt", "r") as infile:
    for line in infile:
        characters += line

for i in characters:
    counter += 1
    if i == "(":
        x += 1
    else:
        x -= 1

    if x < 0:
        print(counter)
        break
