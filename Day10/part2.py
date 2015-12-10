
def repeat(data):
    # Quick hack, so sorry
    data = data + "0"

    iteration = 0
    result = ""

    while iteration < len(data) - 1:
        x = iteration + 1
        character_count = 1
        char = data[iteration]

        while data[x] == char and x < len(data) - 1:
            x = min(x + 1, len(data) - 1)
            character_count += 1

        iteration += character_count
        result += str(character_count) +str(char)
    return result


actualResult = "1113222113"

for i in range(0, 50):
    actualResult = repeat(actualResult)

print(len(actualResult))