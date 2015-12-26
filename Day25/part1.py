
results = [[20151125]]

last_code_added = 20151125

row_requested = 0
column_requested = 0

with open("inputData.txt", "r") as infile:
    for line in infile:
        line = line.split()
        row_requested = int(line[15][:-1])
        column_requested = int(line[17][:-1])

def next_code(code):
    """
    :param code: the previous code in the sequence
    :return: the next code in the sequence
    """
    return (code * 252533) % 33554393

def add_diagonal():
    """
    Adds a diagonal to the results array
    :return: nothing
    """
    global last_code_added
    # A new row is always required for a new diagonal
    results.append([])

    for row in reversed(results):
        last_code_added = next_code(last_code_added)
        row.append(last_code_added)



while len(results) < row_requested:
    # Keep adding diagonals until we have as many rows as we requested
    add_diagonal()

while len(results[row_requested - 1]) < column_requested:
    # Since the last row only has the first column - keep adding more diagonals until we have the column requested
    # for that row.
   add_diagonal()


print(results[row_requested - 1][3075  - 1])