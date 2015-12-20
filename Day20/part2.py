data = ""
elf_counter = {}

with open("inputData.txt", "r") as infile:
    """
    Process inputData.txt and put it into the data array.
    """
    for line in infile:
        data = int(line)


def get_factors(number):
    """
    Note: Taken from Stack Overflow
    http://stackoverflow.com/a/6800214
    :param number: Number to factorize
    :return: Set of factors for this number
    """
    return set(reduce(list.__add__,
                      ([i, number // i] for i in range(1, int(number ** 0.5) + 1) if number % i == 0)))


def get_result(number):
    """
    :param number: House number
    :return: The number of presents in the house of that number
    """
    result = get_factors(number)
    result = remove_unwanted_elves(result)
    register_delivery(result)
    return sum(result) * 11


def remove_unwanted_elves(elves):
    """
    Removes elves that have already delivered to 50 houses
    :param elves: set of elves to check
    :return: new set, with disqualified elves removed
    """
    new_set = elves.copy()
    for elf in elves:
        if elf in elf_counter and elf_counter[elf] >= 50:
            new_set.discard(elf)
    return new_set


def register_delivery(elves):
    """
    Ticks every elf up by 1 in the elf_counter
    :param elves: set of elves to tick up
    :return: nothing
    """
    for elf in elves:
        if elf in elf_counter:
            elf_counter[elf] += 1
        else:
            elf_counter[elf] = 1



result_so_far = 0
ticker = 0
while result_so_far < data:
    ticker += 1
    result_so_far = get_result(ticker)

print("Answer: House #" + str(ticker))
