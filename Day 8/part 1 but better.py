import numpy as np

# use numpy matrices instead of nested lists

class Forest:

    forest = {}
    row_total = 0
    column_total = 0

    def __init__(self, type: str, contents: []) -> None:

        self.type = type

        Forest.forest[self] = contents

        if type == 'row':

            self.num = Forest.row_total

            Forest.row_total += 1



        if type == 'column':

            self.num = Forest.column_total

            Forest.column_total += 1

    

    @staticmethod
    def find_visible_trees(array):

        for row in array:

            previous = None

            for a in range(len(row)):

                if a == 0:

                    row[a].visible = True

                    previous = row[a].height




                elif row[a].height > previous:

                    row[a].visible = True

                    previous = row[a].height


            previous = None

            for b in range(len(row) - 1, -1, -1):

                if b == len(row) - 1:

                    row[b].visible = True

                    previous = row[b].height




                elif row[b].height > previous:

                    row[b].visible = True

                    previous = row[b].height



class Tree:

    def __init__(self, rownum, columnnum, height: int, visible = False) -> None:

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
        
        Forest('row', y)

print('')


Forest.forest = np.array([x for x in Forest.forest.values()])

print(Forest.forest)




Forest.find_visible_trees(Forest.forest)
Forest.find_visible_trees(Forest.forest.T)



count = 0

copy = Forest.forest.copy()

for row in copy:

    for val in row:

        if val.visible:

            count += 1


print(f"number of visible trees: {count}")




# create a bunch of lists containing either 1 or 0 to represent each tree

count2 = 0

for row in Forest.forest:

    temp = []

    for val in row:

        # print(val)

        if val.visible:

            temp.append('1')

            count2 += 1

        else:

            temp.append('0')

    print(f"row: {('').join(temp)}")

print(count2)


# look at line 99, number 7. in that column, while the 0 above the 2 isn't visible, the 3 above the 2 and 0 is visible. this is the flaw in the calculations.