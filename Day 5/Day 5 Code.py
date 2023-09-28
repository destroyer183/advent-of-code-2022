# rearrange the array so that each vertical grid line is a horizontal line with just the letters, with the top-most box at the right
# array should look like this when rearranged properly
# NDMQBPZ
# CLZQMDHV
# QHRDVFZG
# HGDFN
# NFQ
# DQVZFBT
# QMTZDVSH
# MGFPNQ
# BWRM

line1 = ""
line2 = ""
line3 = ""
line4 = ""
line5 = ""
line6 = ""
line7 = ""
line8 = ""
line9 = ""

movecount = 0
movestart = 0
moveend   = 0
countbool = True
startbool = False
endbool   = False

linenum = 1
arraydone = False
y = 0
otherx = ""
memory1 = ""
memory2 = ""

with open("input.txt", "r") as reader:

   for x in reader:

      otherx = x

      x = x.strip()

      print(x)

      
      try:
         if x[0] == "[":
            line1 = otherx[1]  + line1
            line2 = otherx[5]  + line2
            line3 = otherx[9]  + line3
            line4 = otherx[13] + line4
            line5 = otherx[17] + line5
            line6 = otherx[21] + line6
            line7 = otherx[25] + line7
            line8 = otherx[29] + line8
            line9 = otherx[33] + line9

      except IndexError:
         print(line1)
         print(line2)
         print(line3)
         print(line4)
         print(line5)
         print(line6)
         print(line7)
         print(line8)
         print(line9)

      try:
         if x[0] == "1": exit = True
      except IndexError: print(x)  

      def move(movecount, movestart, moveend):
         global line1, line2, line3, line4, line5, line6, line7, line8, line9
         
         for i in range(movecount):
            store1 = movestart
            store2 = moveend
            moveend = movestart[0] + moveend
            movestart = ''.join([movestart[i] for i in range(len(movestart)) if i != 0])
            print("working")
            print(movecount)
            print(movestart)
            print(moveend)
            if line1 == store1: line1 = movestart
            elif line2 == store1: line2 = movestart
            elif line3 == store1: line3 = movestart
            elif line4 == store1: line4 = movestart
            elif line5 == store1: line5 = movestart
            elif line6 == store1: line6 = movestart
            elif line7 == store1: line7 = movestart
            elif line8 == store1: line8 = movestart
            elif line9 == store1: line9 = movestart
            if line1 == store2: line1 = moveend
            elif line2 == store2: line2 = moveend
            elif line3 == store2: line3 = moveend
            elif line4 == store2: line4 = moveend
            elif line5 == store2: line5 = moveend
            elif line6 == store2: line6 = moveend
            elif line7 == store2: line7 = moveend
            elif line8 == store2: line8 = moveend
            elif line9 == store2: line9 = moveend
         print(line1)
         print(line2)
         print(line3)
         print(line4)
         print(line5)
         print(line6)
         print(line7)
         print(line8)
         print(line9)

      y = 0
      try:
         if exit == True: 
            exit = False
            print(x[100])
         while True:
            try:
               while x[y] != "1" and x[y] != "2" and x[y] != "3" and x[y] != "4" and x[y] != "5" and x[y] != "6" and x[y] != "7" and x[y] != "8" and x[y] != "9" and x[y] != "0":
                  print(x[y])
                  y += 1
               print("IT WORKED YESSSSSS")
            except IndexError: print(x)

            if countbool:
               movecount = 0
               while x[y] == "1" or x[y] == "2" or x[y] == "3" or x[y] == "4" or x[y] == "5" or x[y] == "6" or x[y] == "7" or x[y] == "8" or x[y] == "9" or x[y] == "0":
                  movecount = movecount * 10 + int(x[y])
                  y += 1
                  print(movecount)
               countbool = False
               startbool = True

            elif startbool:

               while x[y] == "1" or x[y] == "2" or x[y] == "3" or x[y] == "4" or x[y] == "5" or x[y] == "6" or x[y] == "7" or x[y] == "8" or x[y] == "9" or x[y] == "0":
                  if   x[y] == "1": movestart = line1
                  elif x[y] == "2": movestart = line2
                  elif x[y] == "3": movestart = line3
                  elif x[y] == "4": movestart = line4
                  elif x[y] == "5": movestart = line5
                  elif x[y] == "6": movestart = line6
                  elif x[y] == "7": movestart = line7
                  elif x[y] == "8": movestart = line8
                  elif x[y] == "9": movestart = line9
                  print(movestart)
                  y += 1
               startbool = False
               endbool   = True

            elif endbool:

               while x[y] == "1" or x[y] == "2" or x[y] == "3" or x[y] == "4" or x[y] == "5" or x[y] == "6" or x[y] == "7" or x[y] == "8" or x[y] == "9" or x[y] == "0":
                  if   x[y] == "1": moveend = line1
                  elif x[y] == "2": moveend = line2
                  elif x[y] == "3": moveend = line3
                  elif x[y] == "4": moveend = line4
                  elif x[y] == "5": moveend = line5
                  elif x[y] == "6": moveend = line6
                  elif x[y] == "7": moveend = line7
                  elif x[y] == "8": moveend = line8
                  elif x[y] == "9": moveend = line9
                  print(moveend)
                  y += 1
                  countbool = True

      except IndexError: move(movecount, movestart, moveend)


         
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(movecount)
print(movestart)
print(moveend)



      

      
      




