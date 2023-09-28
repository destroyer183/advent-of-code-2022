letterlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

priority = 0
y = 0
line = 0
charactercount = 0
first = ""
second = ""
third = ""
letter = ""
linesassigned = 0


with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        if first == ""   : first = x
        elif second == "": second = x
        elif third == "" : third = x

        print(first)
        print(second)
        print(third)

        if first != "" and second != "" and third != "":
            for x in list(first):
                if x in list(second) and x in list(third):
                    letter = x
                print(letter)
        
        y = 0
        if first != "" and second != "" and third != "":
            for x in list(letter):
                priority += 1
                while x != letterlist[y]:
                    priority += 1
                    y += 1
                print(priority)

        if first != "" and second != "" and third != "":
            first = ""
            second = ""
            third = ""









    

    





