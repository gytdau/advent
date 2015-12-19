import re

replacements = []
data = ""


with open("inputData.txt", "r") as infile:
    """
    Process inputData.txt and put it into the data array.
    """
    for line in infile:
        line = line.strip().split()
        if not line:
            # Do nothing
            pass
        elif "=>" not in line:
            # This the molecule that we have to build on
            data = "".join(line)
        else:
            # Not nothing, and it has a '=>', so it's data for a possible replacement
            replacements.append([line[0], line[2]])


def delete_from(to_delete, string, pos):
    """
    Deletes instance of 'str' in 'data' at this 'pos'
    :param to_delete: string to be deleted from 'string'
    :param string: string from which 'to_delete' will be deleted
    :param pos: position of 'string' to delete
    """
    data_array = list(string)
    for i in range(len(to_delete)):
        data_array.pop(pos)
    return "".join(data_array)


def replace_at(to_replace, new_replacement, string, pos):
    """
    Replaces 'a' with 'b' at this 'pos'
    :param to_replace: substring of 'string' which needs to be replaced
    :param new_replacement: string which will replace 'to_replace'
    :param string: string which the replacement will be executed on
    :param pos: position of 'new_replacement' in 'string' that should be replaced
    """
    string = delete_from(to_replace, string, pos)
    string = string[:pos] + new_replacement + string[pos:]
    return string




possible_values = []

"""
Main loop
"""

for replacement in replacements:
    # Uses regex to find locations of the replacement we're looking for
    locations = [m.start() for m in re.finditer(replacement[0], data)]

    for location in locations:
        possible_values.append(replace_at(replacement[0], replacement[1], data, location))


print("Answer: " + str(len(set(possible_values))))

