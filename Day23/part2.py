
instructions = []

with open("inputData.txt", "r") as infile:
    """
    Process inputData.txt to insert all the instructions into an array.
    """
    for line in infile:
        instructions.append(line.split())

i = 0
a = 1
b = 0


def execute_line(line):
    """
    Executes the command stored in 'line'.
    :param line: command to execute
    :return: nothing
    """
    if line[0] == "inc":
        inc(line)
        next_instruction()
    elif line[0] == "hlf":
        hlf(line)
        next_instruction()
    elif line[0] == "tpl":
        tpl(line)
        next_instruction()
    elif line[0] == "jmp":
        jmp(line)
    elif line[0] == "jie":
        jie(line)
    elif line[0] == "jio":
        jio(line)


def next_instruction():
    """
    Increments i by 1 to allow execution of next instruction.
    :return: nothing
    """
    global i
    i += 1


def jmp(line):
    global i
    i += int(line[-1])


def hlf(line):
    set_t(line[1], get_t(line[1]) / 2)


def inc(line):
    set_t(line[1], get_t(line[1]) + 1)


def tpl(line):
    set_t(line[1], get_t(line[1]) * 3)


def jio(line):
    if get_t(line[1][:-1]) == 1:
        jmp(line)
    else:
        next_instruction()


def jie(line):
    if get_t(line[1][:-1]) % 2 == 0:
        jmp(line)
    else:
        next_instruction()


def set_t(token, value):
    """
    Sets token to value.
    :param token: register to be set
    :param value: value to set
    :return: nothing
    """
    if token == "a":
        global a
        a = int(value)
    else:
        global b
        b = int(value)


def get_t(token):
    """
    Gets value of token
    :param token: register to get
    :return:
    """
    return a if token == "a" else b


while i < len(instructions):
    execute_line(instructions[i])

"""
These instructions are mysterious. Are they implying Jane Marie was trapped somewhere, and the code released her?
What are we being distracted from?
If Advent of Code starts becoming weirdly morbid, my christmas will be ruined.
"""

print("Answer: " + str(b))
