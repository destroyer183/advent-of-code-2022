

# use a dict full of arrays to represent each row and column

class Forest:

    def __init__(self, row, column) -> None:

        self.row = row
        self.column = column



class Tree:

    def __init__(self, row, column) -> None:

        self.row = row
        self.column = column



with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        print(f"line: {x}")