


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

    def __init__(self, rownum, columnnum, height: int, visible = None, score = {}) -> None:

        if score == {}:

            self.score = {'total': 0, 'north': 0, 'east': 0, 'south': 0, 'west': 0}

        self.rownum = rownum
        self.columnnum = columnnum
        self.height = height
        self.visible = visible



    def check_height(self, tree, direction: str) -> bool:

        if int(tree.height) < int(self.height):

            self.score[direction] += 1

        elif int(tree.height) <= int(self.height):

            self.score[direction] += 1

            return True
        


    def total_score(self):

        self.score['total'] = self.score['north'] * self.score['east'] * self.score['south'] * self.score['west']
        


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

    temp = []

    for i in e:

        temp.append(i.height)

    print(f"column: {('').join(temp)}")


print('')




# assume every tree shorter than current tree is visible

for keys, values in Forest.forest.items():

    for index, key in enumerate(values):

        tree = key

        if keys.type == 'row':

            for a in range(index + 1, len(values)):

                if tree.check_height(values[a], 'east'): break



            for b in range(index - 1, -1, -1):

                if tree.check_height(values[b], 'west'): break



            # print(f"tree height: {tree.height}")
            # print(f"tree index: {tree.rownum}")
            # print(f"score: {tree.score}")



        if keys.type == 'column':

            for c in range(index + 1, len(values)):

                if tree.check_height(values[c], 'south'): break



            for d in range(index - 1, -1, -1):

                if tree.check_height(values[d], 'north'): break



for value in Forest.forest.values():

    for tree in value:

        tree.total_score()



max_score = {'total': 0}

height = 0

tree_location = []

row = ''
column = ''

for value in Forest.forest.values():

    for tree in value:

        if tree.score['total'] > max_score['total']:

            max_score = tree.score

            height = tree.height

            tree_location = []

            tree_location.append(str(tree.rownum))
            tree_location.append(str(tree.columnnum))


for key in Forest.forest:

    if key.type == 'row' and key.num == 61:

        temp = []

        for value in Forest.forest[key]:

            temp.append(value.height)

        row = ('').join(temp)


    
    if key.type == 'column' and key.num == 61:

        temp = []

        for value in Forest.forest[key]:

            temp.append(value.height)

        column = ('').join(temp)



    


print(f"max score: {max_score}")
print(f"height: {height}")
print(f"location: ({(', ').join(tree_location)})")
print(f"row: {row}")
print(f"column: {column}")


