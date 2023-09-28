

with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        x = [i for i in x]

        last_14_chars = x[0:14]

        e = last_14_chars

        print(e)

        for i in range(14, len(x)):

            for key, a in enumerate(e):

                temp = [b for b in e]

                temp.pop(key)

                if a not in temp:

                    done = True

                if a in temp:

                    done = False

                    e.pop(0)
                    e.append(x[i])

                    break



            if done: 
                
                print(f"string: {e}")

                print(f"index: {i}")

                break