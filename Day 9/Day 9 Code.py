import numpy as np



# use vstack function in numpy to create 2D lists (matrices)


with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        x = x.split(" ")

        print(f"line: {x}")