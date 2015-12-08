import re

lines = []

with open("inputData.txt", "r") as infile:
    for line in infile:
        lines.append(line.replace('\n', '').replace('\r', ''))

codeLetters = 0
escapedLetters = 0

for line in lines:
    codeLetters += len(line)

    escaped = re.escape(line)
    escapedLetters += len(escaped) + 2 # + 2 for the two quotes we didn't add


difference = escapedLetters - codeLetters
print(str(difference))
