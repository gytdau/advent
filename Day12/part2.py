import json

with open("inputData.txt", "r") as infile:
    for line in infile:
        data = line

captured = json.loads(data)

def main_loop(object):
    if type(object) == int:
        # It's an int, we can just return it
        return object
    elif type(object) == list:
        # It's a list, we'll have to sum it recursively
        sub_objects = [main_loop(sub_object) for sub_object in object]
        return sum(sub_objects)
    elif type(object) != dict or "red" in object.values():
        # It's something else or there's 'red' in the object
        return 0
    else:
        #It's a dict, we'll have to sum it recursively too
        return main_loop(list(object.values()))

print(main_loop(captured))