
ingredients = []


with open("inputData.txt", "r") as infile:
    for line in infile:
        line = line.split()
        ingredients.append(
                [
                    int(line[2][:-1]),
                    int(line[4][:-1]),
                    int(line[6][:-1]),
                    int(line[8][:-1])

                ]
        )


top_score = 0

# This is really bad.

for a in range(100):
    for b in range(100 ):
        for c in range(100):
            # Thank you, Eric, for only giving us four ingredients
            if a + b + c <= 100:
                d = 100 - a - b - c

                # This is also really terrible - it should be done with a For loop instead
                score = max(0,
                               ingredients[0][0] * a +
                               ingredients[1][0] * b +
                               ingredients[2][0] * c +
                               ingredients[3][0] * d) * max(0,
                               ingredients[0][1] * a +
                               ingredients[1][1] * b +
                               ingredients[2][1] * c +
                               ingredients[3][1] * d) * max(0,
                               ingredients[0][2] * a +
                               ingredients[1][2] * b +
                               ingredients[2][2] * c +
                               ingredients[3][2] * d) * max(0,
                               ingredients[0][3] * a +
                               ingredients[1][3] * b +
                               ingredients[2][3] * c +
                               ingredients[3][3] * d)

                top_score = max(top_score, score)




print(top_score)