import re

with open("inputData.txt", "r") as infile:
    for line in infile:
        data = line

captured = re.findall("([-]?[0-9]+)", data)

captured = list(map(int, captured))

print(sum(captured))