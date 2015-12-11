alphabet = list(map(chr, range(97, 123)))

dataInput = "hxbxwxba"

def increment(a):
    a_number = letter_number(a)
    if a_number == 25:
        return "a"

    return alphabet[a_number + 1]


def full_increment(a):
    should_increment = True
    i = len(a) - 1
    while should_increment:
        new_letter = increment(a[i])
        a_2 = list(a)
        a_2[i] = new_letter
        a = ''.join(a_2)

        i -= 1

        if not new_letter == "a":
            should_increment = False

    return a


# Test `a` against the rules

# 'Passwords must include one increasing straight of at least three letters'
def rule_one(a):
    for i in range(len(a)-2):
        letters = [letter_number(a[i]), letter_number(a[i+1]), letter_number(a[i+2])]
        if letters[1] == letters[0] + 1 and letters[2] == letters[0] + 2:
            return True
    return False

# 'Passwords may not contain the letters i, o, or l'
def rule_two(a):
    return not("i" in a or "o" in a or "l" in a)

# 'Passwords must contain at least two different, non-overlapping pairs of letters'
def rule_three(a):
    pairs = 0
    incrementer = 0
    while incrementer < len(a) - 2:
        incrementer += 1
        if a[incrementer] == a[incrementer + 1]:
            pairs += 1
            incrementer += 1

    return pairs >= 2

def all_rules(a):
    return rule_one(a) and rule_two(a) and rule_three(a)

def letter_number(a):
    return alphabet.index(a)

def next_password(a):
    password = a
    while not all_rules(password):
        password = full_increment(password)
    return password


print(next_password(dataInput))