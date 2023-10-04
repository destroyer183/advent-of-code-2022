

# use a dict full of arrays to represent each row and column

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



row1 = '102200120221123133322123221134224301040024344534431245323303212210030001244234132301200020310012011'
row2 = '210101220131232022104432220132221131234351145114524135253112332342312410211104233102330122201111010'


listvalues = [row1, row2]


for index, x in enumerate(listvalues):

    x = x.strip()

    x = [y for y in x]

    y = []

    for i in range(len(x)):
        
        y.append(Tree(Forest.row_total, i, x[i]))
        
    Forest('row', y)



for i in range(len(Forest.forest)):

    x = [x[i] for x in Forest.forest.values()]

    Forest('column', x)



x = list(Forest.forest.values())[0][0]

print(x.height)

y = list(Forest.forest.values())[2][1]

print(y.height)

copy = Forest.forest.copy()

names = list(copy.keys())

print(f"type: {type(Forest.forest)}")

print(names[0])

print(Forest.forest[names[0]][0])

print(Forest.forest[names[0]][0].height)

Forest.forest[names[0]][0].visible = True

print(Forest.forest[names[0]][0].visible)

print(Forest.forest[names[2]][0].visible)

Forest.forest[names[2]][0].visible = False

print(Forest.forest[names[0]][0].visible)

print(Forest.forest[names[2]][0].visible)