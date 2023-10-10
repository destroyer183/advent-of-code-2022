import numpy as np



# use vstack function in numpy to create 2D lists (matrices)

max_u = 0
max_r = 0
max_d = 0
max_l = 0
current = [0, 0]

with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        x = x.split(" ")

        print(f"line: {x}")

        if x[0] == 'U':

            current[1] += x[1]

            if current[1] > max_u:

                max_u = current[1]

        

        if x[0] == 'R':

            current[0] += x[1]

            if current[0] > max_r:

                max_r = current[0]



        if x[0] == 'D':

            current[1] -= x[1]

            if current[1] < max_d * -1:

                max_d = current[1]



        if x[0] == 'L':

            current[0] += x[1]

            if current[0] < max_l * -1:

                max_l = current[0] * -1



class Grid:

    grid = np.array(max_u + max_d, max_r + max_l)

    def __init__(self) -> None:

        pass


Grid.grid[max_u, max_l] = 's'



with open("input.txt", "r") as reader:

    for x in reader:
        
        x = x.strip()
        
        x = x.split(" ")

