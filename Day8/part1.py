
lines = []

with open("inputData.txt", "r") as infile:
    for line in infile:
        lines.append(line.replace('\n', '').replace('\r', ''))

realLetters = 0
codeLetters = 0

for line in lines:
    codeLetters += len(line)

    lineWithoutQuotes = line[1:-1]
    decodedString = bytes(lineWithoutQuotes, "utf-8").decode("unicode_escape")
    realLetters += len(decodedString)


difference = codeLetters - realLetters
print(str(difference))
