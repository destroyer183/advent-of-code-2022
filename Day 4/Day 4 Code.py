# compare the first and second numbers of each pair, and figure out which is larger or smaller.

y = 0
x1 = ""
y1 = ""
x2 = ""
y2 = ""
rangenum = 0
recall = ""
count = 0




with open("input.txt", "r") as reader:

   for x in reader:

      x = x.strip()

      print(x)

      recall = x

      y = 0
      x1 = ""
      y1 = ""
      x2 = ""
      y2 = ""
      rangenum = 0

      if x[y] != "":
            x = int(x[y])
            
            while x == int(x):
                  x = str(x)

                  x = recall

                  try:
                        if x[y] == "-" or x[y] == ",": 
                              y += 1
                              rangenum += 1
                  except IndexError: break

                  if rangenum == 0  : x1 += x[y]
                  elif rangenum == 1: y1 += x[y]
                  elif rangenum == 2: x2 += x[y]
                  elif rangenum == 3: y2 += x[y]

                  if rangenum == 4: break

                  x = int(x[y])
                  y += 1

      if int(x1) <= int(x2) and int(y1) >= int(y2):
            count += 1
            problem = True

      
      elif int(x1) >= int(x2) and int(y1) <= int(y2): 
            count += 1
            problem = True

      print(x1)
      print(y1)
      print(x2)
      print(y2)
      try:
            print(problem)
      except:pass
      problem = False

print(count)
      



   


