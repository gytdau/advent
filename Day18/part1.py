
lights = []

with open("inputData.txt", "r") as infile:
    """
    Process inputData.txt and put it into the data array.
    """
    for line in infile:
        line = list(line.strip())
        lights.append([1 if char == "#" else 0 for char in line])


def get_light(x, y):
    """
    Returns light value at X, Y, or 0 if that light doesn't exist.
    :param x: position X
    :param y: position Y
    :return: light value at position X, Y
    """
    return 0 if x < 0 or x > 99 or y < 0 or y > 99 else lights[x][y]


def get_neighbours(x, y):
    """
    Returns the sum of the neighbours of X, Y.
    :param x: position X
    :param y: position Y
    :return: sum of the 8 neighbours of the light at position X, Y
    """
    top = [
        get_light(x-1, y-1),
        get_light(x-1, y),
        get_light(x-1, y+1)
    ]
    middle = [
        get_light(x, y-1),
        get_light(x, y+1)
    ]
    bottom = [
        get_light(x+1, y-1),
        get_light(x+1, y),
        get_light(x+1, y+1)
    ]
    return sum(top) + sum(middle) + sum(bottom)


def get_new_state(x, y):
    """
    Returns 1 or 0, depending on whether this cell should die or live.
    :param x: position X
    :param y: position Y
    :return: desired state
    """
    neighbours = get_neighbours(x, y)
    current_state = get_light(x, y)

    if current_state == 0:
        if neighbours == 3:
            return 1
        else:
            return 0
    else:
        if neighbours == 2 or neighbours == 3:
            return 1
        else:
            return 0


def next_step():
    """
    Processes the next step of the game.
    :return: next step of the lights variable
    """
    new_lights = [[0 for a in range(100)] for b in range(100)]
    for x in range(0, 100):
        for y in range(0, 100):
            new_lights[x][y] = get_new_state(x, y)

    return new_lights


def make_output(lights_to_render):
    """
    Prints out the lights in the desired format. Only a helper function. Not used.
    :param lights_to_render: lights that should be rendered.
    :return: nothing
    """
    output = ""
    for light_strip in lights_to_render:
        for light in light_strip:
            output += "#" if light == 1 else "."
        output += "\n"
    print(output)


# This is where the magic happens.

for iteration in range(100):
    lights = next_step()


result = sum([sum(c) for c in lights])
print(result)
