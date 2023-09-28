letterlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priority = 0
priorityy = 0
y = 0
yy = 0
charactercount = 0
firstline = ""
secondline = ""
first = ""
second = ""
third = ""
letter = ""
lettery = ""
linesassigned = 0


with open("input.txt", "r") as reader:

    for x in reader:
        y = 0
        charactercount = 0
        while x[y] != "\n":
            print(x[y])
            y += 1
            charactercount += 1
        
        charactercount /= 2
        charactercount = int(charactercount)
        
        y = 0

        firstline = ""
        while y < charactercount:
            firstline += x[y]
            y += 1

        print(firstline)

        y = charactercount

        secondline = ""
        while x[y] != "\n":
            secondline += x[y]
            y += 1

        print(secondline)

        y = 0
        counter = 0
        for x in list(firstline):
            if x in list(secondline):
                letter = x

        y = 0
        for x in list(letter):
            priority += 1
            while x != letterlist[y]:
                priority += 1
                y += 1
            print(priority)

print(priority)