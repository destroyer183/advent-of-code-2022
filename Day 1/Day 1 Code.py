currentcalories = 0
maxcalories1 = 0
maxcalories2 = 0
maxcalories3 = 0

with open("input.txt", "r") as reader:

    for x in reader:
        x = x.strip()
        print(x)

        if x == "":
            if currentcalories > maxcalories1: 
                maxcalories3 = maxcalories2
                maxcalories2 = maxcalories1
                maxcalories1 = currentcalories

            elif currentcalories > maxcalories2:
                maxcalories3 = maxcalories2
                maxcalories2 = currentcalories
            
            elif currentcalories > maxcalories3: maxcalories3 = currentcalories

            currentcalories = 0
        else:
            currentcalories += int(x)

print(maxcalories3)
print(maxcalories2)
print(maxcalories1)
print(maxcalories1 + maxcalories2 + maxcalories3)