

# use a dict full of arrays to represent each row and column
# ADD HEIGHT TO TREE CLASS

class Forest:

    forest = {}
    row_total = 0
    column_total = 0

    def __init__(self, type: str, contents: []) -> None:

        self.type = type

        if type == 'row':

            self.num = Forest.row_total

            Forest.forest[self] = contents

            Forest.row_total += 1



        if type == 'column':

            self.num = Forest.column_total

            Forest.forest[self] = contents

            Forest.column_total += 1



class Tree:

    def __init__(self, rownum, columnnum, height: int, visible = None) -> None:

        self.rownum = rownum
        self.columnnum = columnnum
        self.height = height
        self.visible = visible



with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        print(f"line: {x}")

        x = [y for y in x]

        y = []

        for i in range(len(x)):
        
            y.append(Tree(Forest.row_total, i, x[i]))
        
        Forest('row', x)



for i in range(len(Forest.forest)):

    x = [x[i] for x in Forest.forest.values()]

    Forest('column', x)



# the whole dict is now correctly filled, next, whether each tree is visible or not needs to be computed.