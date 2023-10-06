

# use a dict full of arrays to represent each row and column
# ADD HEIGHT TO TREE CLASS

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
        
            y.append(Forest.row_total, i, Tree(x[i]))
        
        Forest('row', y)

print('')

for key in Forest.forest:

    temp = []

    for val in Forest.forest[key]:

        temp.append(val.height)

    print(f"row: {('').join(temp)}")



x = []

for i in range(len(Forest.forest)):

    x.append([x[i] for x in Forest.forest.values()])



for e in x:

    Forest('column', e)

print('')

for key in Forest.forest:

    previous = None

    for a in range(len(Forest.forest[key])):

        if a == 0:

            Forest.forest[key][a].visible = True

            previous = Forest.forest[key][a].height




        elif Forest.forest[key][a].height > previous:

            Forest.forest[key][a].visible = True

            previous = Forest.forest[key][a].height


    previous = None

    for b in range(len(Forest.forest[key]) - 1, -1, -1):

        if b == len(Forest.forest[key]) - 1:

            Forest.forest[key][b].visible = True

            previous = Forest.forest[key][b].height




        elif Forest.forest[key][b].height > previous:

            Forest.forest[key][b].visible = True

            previous = Forest.forest[key][b].height




count = 0

copy = Forest.forest.copy()

for key in copy:

    if key.type == 'row':

        for val in copy[key]:

            if val.visible:

                count += 1


print(f"number of visible trees: {count}")




# create a bunch of lists containing either 1 or 0 to represent each tree

count2 = 0

for key in Forest.forest:

    temp = []

    if key.type == 'row':

        for val in Forest.forest[key]:

            # print(val)

            if val.visible:

                temp.append('1')

                count2 += 1

            else:

                temp.append('0')

        print(f"row: {('').join(temp)}")

print(count2)


# look at line 99, number 7. in that column, while the 0 above the 2 isn't visible, the 3 above the 2 and 0 is visible. this is the flaw in the calculations.