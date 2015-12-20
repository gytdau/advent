data = ""

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
    return sum(get_factors(number)) * 10


result = 0
ticker = 0
while result < data:
    ticker += 1
    result = get_result(ticker)

print("Answer: House #" + str(ticker))
