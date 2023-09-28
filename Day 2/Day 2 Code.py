score1 = 0
score2 = 0

with open("input.txt", "r") as reader:

    for x in reader:
    
        x = x.strip()

        one = x[0]
        two = x[2]

        if one == "A" and two == "X"  : score1 += 4
        elif one == "A" and two == "Y": score1 += 8
        elif one == "A" and two == "Z": score1 += 3
        elif one == "B" and two == "X": score1 += 1
        elif one == "B" and two == "Y": score1 += 5
        elif one == "B" and two == "Z": score1 += 9
        elif one == "C" and two == "X": score1 += 7
        elif one == "C" and two == "Y": score1 += 2
        elif one == "C" and two == "Z": score1 += 6

        if one == "A" and two == "X"  : score2 += 3
        elif one == "A" and two == "Y": score2 += 4
        elif one == "A" and two == "Z": score2 += 8
        elif one == "B" and two == "X": score2 += 1
        elif one == "B" and two == "Y": score2 += 5
        elif one == "B" and two == "Z": score2 += 9
        elif one == "C" and two == "X": score2 += 2
        elif one == "C" and two == "Y": score2 += 6
        elif one == "C" and two == "Z": score2 += 7

print(score1)
print(score2)