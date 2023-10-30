import numpy as np



# use vstack function in numpy to create 2D lists (matrices)

max_u = 0
max_r = 0
max_d = 0
max_l = 0

total_u = 0
total_r = 0
total_d = 0
total_l = 0
current = [0, 0]

max_current0 = 0
max_current1 = 0

file = []

count = 0

with open("input.txt", "r") as reader:

    for x in reader:

        count += 1

        file.append(x)

        x = x.strip()

        x = x.split(" ")

        # print(f"line: {x}")

        if x[0] == 'U':

            current[1] -= int(x[1])

            total_u += int(x[1])

            if current[1] < max_u:

                max_u = current[1]

        

        if x[0] == 'R':

            current[0] += int(x[1])

            total_r += int(x[1])

            if current[0] > max_r:

                max_r = current[0]



        if x[0] == 'D':

            current[1] += int(x[1])

            total_d += int(x[1])

            if current[1] > max_d:

                max_d = current[1]



        if x[0] == 'L':

            current[0] -= int(x[1])

            total_l += int(x[1])

            if current[0] < max_l:

                max_l = current[0]



class Knot:

    grid = np.ndarray(shape=(max_r + (max_l * -1), max_d + (max_u * -1)), dtype=str)
    previous = None
    tails = []
    num = 0

    def __init__(self, position = [(max_l * -1), (max_u * -1)]) -> None:

        self.position = position
        self.parent = Knot.previous
        self.num = Knot.num
        Knot.num += 1

        if Knot.previous is not None: 

            Knot.tails.append(self)

        Knot.previous = self
        


    def move(self, direction, distance):

        if direction == 'U': index = 1; incrament = -1
        if direction == 'R': index = 0; incrament = 1
        if direction == 'D': index = 1; incrament = 1
        if direction == 'L': index = 0; incrament = -1

        for i in range(int(distance)):

            head.position[index] += incrament

            for item in Knot.tails:

                item.follow()



    def follow(self):

        # print(f"parent location: {self.parent.position}, tail location: {self.position}")

        distance = [self.parent.position[0] - self.position[0], self.parent.position[1] - self.position[1]]

        # print(f"distance: {distance}")

        if distance[0] > 1 or distance[0] < -1 or distance[1] > 1 or distance[1] < -1:

            if distance[0] >  1: distance[0] -= 1
            if distance[0] < -1: distance[0] += 1
            if distance[1] >  1: distance[1] -= 1
            if distance[1] < -1: distance[1] += 1

            self.position[0] += distance[0]
            self.position[1] += distance[1]

            self.track()



    def track(self):

        if self.num == len(Knot.tails):

            # print(f"position 0: {self.position[0] - 1}\nposition 1: {self.position[1] - 1}")

            Knot.grid[self.position[0] - 1, self.position[1] - 1] = '#'

            # print(f"new tile: {Knot.grid[self.position[0] - 1, self.position[1] - 1]}") # this prints a blank space, how tf does this not print #

        

Knot.grid = np.array([x for x in Knot.grid])

Knot.grid[(max_l * -1), (max_u * -1)] = 's'



head = Knot([(max_l * -1), (max_u * -1)])

for i in range(9):

    Knot([(max_l * -1), (max_u * -1)])



print(f"grid:\n{Knot.grid}\nshape: {Knot.grid.shape}\n")

print(f"max u: {max_u}\nmax r: {max_r}\nmax d: {max_d}\nmax l: {max_l}\n")

print(f"total u: {total_u}\ntotal r: {total_r}\ntotal d: {total_d}\ntotal l: {total_l}\n")

print(f"shape: {Knot.grid.shape}")

print(f"current: {current}")

print(f"number of knots: {len(Knot.tails)}")




# maybe set the number of knots to 2, and then print a grid of the knot locations at each step to make sure they are all moving correctly.




count = 0

with open("input.txt", "r") as read:

    for x in read:

        count += 1
        
        x = x.strip()
        
        x = x.split(" ")

        # print(f"line: {x}")

        head.move(x[0], x[1])

print(f"count: {count}")



count = 1

for item in np.nditer(Knot.grid):

    if item == '#': count += 1

print(f"count: {count}")