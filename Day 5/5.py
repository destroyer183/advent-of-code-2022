#     [B]             [B] [S]        
#     [M]             [P] [L] [B] [J]
#     [D]     [R]     [V] [D] [Q] [D]
#     [T] [R] [Z]     [H] [H] [G] [C]
#     [P] [W] [J] [B] [J] [F] [J] [S]
# [N] [S] [Z] [V] [M] [N] [Z] [F] [M]
# [W] [Z] [H] [D] [H] [G] [Q] [S] [W]
# [B] [L] [Q] [W] [S] [L] [J] [W] [Z]
#  1   2   3   4   5   6   7   8   9 
# array for stack 1
stack1_ = ['B', 'W', 'N']
# array for stack 2
stack2_ = ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B']
# array for stack 3
stack3_ = ['Q', 'H', 'Z', 'W', 'R']
# array for stack 4
stack4_ = ['W','D','V', 'J', 'Z', 'R']
#stack 5
stack5_=['S','H','M','B']
# array for stack 6
stack6_ = ['L', 'G', 'N', 'J', 'H','V','P','B']
# array for stack 7
stack7_ = ['J', 'Q', 'Z', 'F','H','D','L','S']
# array for stack 8
stack8_=['W','S','F','J','G','Q', 'B']
# array for stack 9
stack9_=['Z','W','M','S', 'C', 'D', 'J']
#function to move the last n numbers of elements of the array to the last one in the target array with no return value
def move(n, source, target):
    # for example if n=3, then the last 3 elements of the source array will be moved to the last element of the target array. First the last one is moved to the target array, then the second last one, then the third last one.
    for i in range(n):
        target.append(source.pop())
    #print the last element of each array
    # print(stack1_[-1], stack2_[-1], stack3_[-1], stack4_[-1], stack5_[-1], stack6_[-1], stack7_[-1], stack8_[-1], stack9_[-1])


#instructions:
move(3, stack5_, stack2_);
move(5, stack3_, stack1_); 
move(4, stack4_, stack9_)
move(6, stack1_, stack4_)
move(6, stack8_, stack7_)
move(5, stack2_, stack7_)
move(1, stack5_, stack4_)
move(11,stack9_, stack7_)
move(1, stack1_, stack9_)
move(6, stack4_, stack6_)
move(12, stack6_, stack7_)
move(1, stack9_, stack2_)
move(2, stack4_, stack6_)
move(1, stack8_, stack9_)
move(1, stack9_, stack4_)
move(1, stack6_, stack1_)
move(2, stack7_, stack5_)
move(2, stack6_, stack7_)
move(2, stack1_, stack6_)
move(2, stack4_, stack7_)
move(1, stack5_, stack4_)
move(1, stack5_, stack6_)
move(1, stack6_, stack1_)
move(1, stack1_, stack3_)
move(1, stack4_, stack1_)
move(1, stack1_, stack4_)
move(1, stack4_, stack5_)
move(1, stack3_, stack9_)
move(1, stack5_, stack1_)
move(4, stack2_, stack1_)
move(20, stack7_, stack8_)
move(24, stack7_, stack3_)
move(3, stack6_, stack4_)
move(1, stack1_, stack9_)
move(1, stack9_, stack3_)
move(2, stack1_, stack2_)
move(2, stack4_, stack1_)
move(2, stack2_, stack1_)
move(14, stack3_, stack6_)
move(6, stack1_, stack6_)
move(10, stack3_, stack2_)
move(1, stack2_, stack3_)
move(6, stack6_, stack5_)
move(2, stack3_, stack4_)
move(13, stack8_, stack4_)
move(1, stack9_, stack7_)
move(1, stack6_, stack3_)
move(10, stack4_, stack2_)
move(1, stack3_, stack6_)
move(2, stack8_, stack7_)
move(1, stack7_, stack2_)
move(11,stack6_, stack8_)
move(2, stack6_, stack1_)
move(2, stack1_, stack3_)
move(1, stack8_, stack6_)
move(1, stack3_, stack9_)
move(3, stack8_, stack2_)
move(1, stack3_, stack6_)
move(2, stack6_, stack4_)
move(1, stack6_, stack5_)
move(11,stack2_, stack9_)
move(2, stack4_, stack6_)
move(1, stack6_, stack1_)
move(1, stack1_, stack5_)
move(11,stack2_, stack7_)
move(12, stack7_, stack5_)
move(1, stack6_, stack2_)
move(10, stack8_, stack7_)
move(6, stack5_, stack3_)
move(4, stack5_, stack4_)
move(11,stack9_, stack7_)
move(7, stack4_, stack9_)
move(4, stack9_, stack6_)
move(12, stack7_, stack3_)
move(1, stack8_, stack9_)
move(1, stack5_, stack1_)
move(1, stack1_, stack2_)
move(1, stack6_, stack9_)
move(3, stack4_, stack1_)
move(1, stack9_, stack7_)
move(8, stack7_, stack2_)
move(3, stack6_, stack1_)
move(8, stack2_, stack3_)
move(1, stack7_, stack4_)
move(2, stack7_, stack2_)
move(1, stack5_, stack2_)
move(8, stack5_, stack1_)
move(3, stack9_, stack6_)
move(1, stack6_, stack2_)
move(1, stack4_, stack5_)
move(1, stack5_, stack4_)
move(2, stack9_, stack3_)
move(1, stack8_, stack6_)
move(1, stack4_, stack5_)
move(1, stack5_, stack1_)
move(1, stack6_, stack8_)
move(1, stack8_, stack1_)
move(7, stack1_, stack5_)
move(11,stack3_, stack7_)
move(1, stack1_, stack9_)
move(4, stack2_, stack1_)
move(5, stack1_, stack3_)
move(1, stack5_, stack9_)
move(1, stack6_, stack3_)
move(6, stack2_, stack1_)
move(5, stack7_, stack3_)
move(1, stack6_, stack8_)
move(1, stack8_, stack4_)
move(6, stack7_, stack9_)
move(4, stack9_, stack8_)
move(2, stack8_, stack9_)
move(2, stack5_, stack8_)
move(13, stack3_, stack7_)
move(1, stack3_, stack8_)
move(2, stack1_, stack9_)
move(3, stack1_, stack5_)
move(1, stack4_, stack1_)
move(6, stack5_, stack9_)
move(8, stack9_, stack8_)
move(2, stack7_, stack3_)
move(1, stack9_, stack7_)
move(1, stack5_, stack2_)
move(5, stack9_, stack8_)
move(1, stack8_, stack7_)
move(1, stack2_, stack9_)
move(7, stack1_, stack2_)
move(4, stack7_, stack5_)
move(6, stack2_, stack3_)
move(1, stack2_, stack1_)
move(10, stack8_, stack9_)
move(3, stack8_, stack9_)
move(4, stack5_, stack1_)
move(2, stack8_, stack6_)
move(9, stack9_, stack8_)
move(1, stack9_, stack6_)
move(8, stack8_, stack4_)
move(12, stack3_, stack5_)
move(1, stack4_, stack2_)
move(3, stack8_, stack1_)
move(3, stack9_, stack7_)
move(1, stack3_, stack2_)
move(1, stack6_, stack9_)
move(8, stack3_, stack8_)
move(6, stack4_, stack5_)
move(1, stack7_, stack6_)
move(1, stack8_, stack1_)
move(6, stack8_, stack7_)
move(1, stack3_, stack6_)
move(7, stack1_, stack5_)
move(1, stack4_, stack9_)
move(4, stack6_, stack5_)
move(13, stack7_, stack5_)
move(1, stack8_, stack2_)
move(2, stack9_, stack3_)
move(4, stack7_, stack2_)
move(1, stack3_, stack8_)
move(1, stack3_, stack4_)
move(4, stack1_, stack2_)
move(1, stack5_, stack7_)
move(23, stack5_, stack6_)
move(1, stack8_, stack6_)
move(1, stack9_, stack4_)
move(5, stack2_, stack6_)
move(1, stack4_, stack9_)
move(1, stack9_, stack3_)
move(1, stack7_, stack8_)
move(1, stack4_, stack3_)
move(1, stack3_, stack7_)
move(1, stack7_, stack5_)
move(1, stack8_, stack7_)
move(12, stack6_, stack1_)
move(1, stack2_, stack5_)
move(1, stack3_, stack1_)
move(20, stack5_, stack2_)
move(14, stack2_, stack4_)
move(11,stack2_, stack6_)
move(1, stack7_, stack8_)
move(13, stack1_, stack8_)
move(9, stack8_, stack4_)
move(3, stack8_, stack6_)
move(10, stack6_, stack8_)
move(6, stack6_, stack4_)
move(4, stack8_, stack5_)
move(26, stack4_, stack2_)
move(2, stack5_, stack2_)
move(5, stack8_, stack1_)
move(1, stack8_, stack3_)
move(2, stack1_, stack3_)
move(2, stack3_, stack7_)
move(27, stack2_, stack7_)
move(2, stack8_, stack1_)
move(1, stack3_, stack7_)
move(6, stack6_, stack2_)
move(4, stack6_, stack1_)
move(4, stack6_, stack4_)
move(2, stack5_, stack4_)
move(4, stack2_, stack1_)
move(3, stack1_, stack8_)
move(1, stack2_, stack8_)
move(8, stack4_, stack3_)
move(1, stack2_, stack8_)
move(5, stack8_, stack6_)
move(1, stack4_, stack2_)
move(1, stack2_, stack1_)
move(6, stack3_, stack1_)
move(13, stack7_, stack1_)
move(1, stack2_, stack8_)
move(1, stack8_, stack2_)
move(1, stack6_, stack2_)
move(1, stack2_, stack8_)
move(1, stack8_, stack2_)
move(14, stack7_, stack1_)
move(5, stack6_, stack3_)
move(2, stack3_, stack1_)
move(3, stack3_, stack2_)
move(3, stack7_, stack4_)
move(1, stack4_, stack9_)
move(1, stack9_, stack7_)
move(2, stack3_, stack6_)
move(5, stack2_, stack7_)
move(1, stack7_, stack6_)
move(5, stack7_, stack6_)
move(2, stack6_, stack7_)
move(1, stack6_, stack8_)
move(1, stack4_, stack7_)
move(4, stack6_, stack9_)
move(35, stack1_, stack8_)
move(3, stack7_, stack2_)
move(1, stack2_, stack5_)
move(24, stack8_, stack3_)
move(1, stack5_, stack8_)
move(13, stack3_, stack6_)
move(2, stack2_, stack6_)
move(6, stack6_, stack4_)
move(11,stack1_, stack6_)
move(12, stack6_, stack1_)
move(1, stack8_, stack1_)
move(2, stack1_, stack3_)
move(5, stack4_, stack1_)
move(1, stack6_, stack4_)
move(1, stack8_, stack3_)
move(13, stack3_, stack9_)
move(3, stack8_, stack2_)
move(3, stack2_, stack7_)
move(1, stack3_, stack6_)
move(3, stack7_, stack8_)
move(14, stack1_, stack3_)
move(1, stack1_, stack9_)
move(6, stack3_, stack8_)
move(17, stack8_, stack6_)
move(1, stack3_, stack7_)
move(1, stack7_, stack8_)
move(26, stack6_, stack7_)
move(1, stack1_, stack9_)
move(3, stack4_, stack1_)
move(2, stack3_, stack8_)
move(1, stack8_, stack4_)
move(14, stack9_, stack7_)
move(12, stack7_, stack3_)
move(2, stack1_, stack4_)
move(2, stack7_, stack8_)
move(2, stack8_, stack3_)
move(4, stack9_, stack8_)
move(1, stack4_, stack7_)
move(1, stack1_, stack3_)
move(2, stack4_, stack2_)
move(24, stack7_, stack6_)
move(1, stack8_, stack1_)
move(1, stack7_, stack2_)
move(1, stack7_, stack9_)
move(3, stack2_, stack9_)
move(1, stack1_, stack6_)
move(5, stack8_, stack2_)
move(5, stack3_, stack4_)
move(1, stack2_, stack5_)
move(3, stack9_, stack8_)
move(2, stack4_, stack9_)
move(16, stack6_, stack3_)
move(14, stack3_, stack8_)
move(1, stack7_, stack9_)
move(8, stack6_, stack9_)
move(4, stack8_, stack5_)
move(8, stack8_, stack3_)
move(1, stack5_, stack8_)
move(1, stack2_, stack4_)
move(4, stack8_, stack7_)
move(1, stack5_, stack6_)
move(12, stack9_, stack5_)
move(15, stack5_, stack8_)
move(1, stack6_, stack1_)
move(2, stack2_, stack6_)
move(3, stack4_, stack2_)
move(4, stack2_, stack7_)
move(8, stack7_, stack3_)
move(1, stack1_, stack4_)
move(3, stack6_, stack9_)
move(16, stack8_, stack3_)
move(3, stack9_, stack4_)
move(1, stack8_, stack9_)
move(2, stack9_, stack4_)
move(24, stack3_, stack8_)
move(19, stack8_, stack7_)
move(2, stack8_, stack7_)
move(7, stack4_, stack5_)
move(13, stack7_, stack5_)
move(4, stack7_, stack8_)
move(7, stack8_, stack1_)
move(3, stack5_, stack3_)
move(3, stack7_, stack2_)
move(1, stack1_, stack4_)
move(1, stack7_, stack2_)
move(3, stack2_, stack4_)
move(8, stack3_, stack1_)
move(11,stack1_, stack3_)
move(12, stack3_, stack4_)
move(1, stack2_, stack5_)
move(18, stack3_, stack8_)
move(3, stack1_, stack9_)
move(1, stack3_, stack5_)
move(15, stack5_, stack4_)
move(4, stack5_, stack1_)
move(23, stack4_, stack6_)
move(3, stack1_, stack6_)
move(13, stack8_, stack3_)
move(25, stack6_, stack2_)
move(1, stack9_, stack5_)
move(5, stack3_, stack8_)
move(17, stack2_, stack8_)
move(4, stack4_, stack1_)
move(1, stack9_, stack7_)
move(5, stack2_, stack6_)
move(2, stack2_, stack4_)
move(1, stack9_, stack4_)
move(6, stack3_, stack9_)
move(16, stack8_, stack3_)
move(2, stack1_, stack8_)
move(1, stack7_, stack4_)
move(5, stack4_, stack7_)
move(1, stack5_, stack3_)
move(2, stack7_, stack1_)
move(9, stack8_, stack4_)
move(3, stack7_, stack2_)
move(2, stack8_, stack3_)
move(10, stack4_, stack1_)
move(1, stack2_, stack3_)
move(5, stack3_, stack7_)
move(2, stack8_, stack9_)
move(2, stack9_, stack8_)
move(1, stack2_, stack1_)
move(3, stack9_, stack6_)
move(2, stack2_, stack8_)
move(4, stack7_, stack3_)
move(4, stack8_, stack6_)
move(1, stack7_, stack1_)
move(1, stack4_, stack8_)
move(4, stack3_, stack4_)
move(4, stack4_, stack2_)
move(6, stack1_, stack2_)
move(1, stack4_, stack3_)
move(5, stack3_, stack8_)
move(6, stack3_, stack8_)
move(2, stack2_, stack8_)
move(3, stack2_, stack9_)
move(8, stack1_, stack6_)
move(3, stack2_, stack7_)
move(2, stack7_, stack2_)
move(13, stack6_, stack5_)
move(7, stack5_, stack9_)
move(3, stack2_, stack7_)
move(1, stack2_, stack9_)
move(2, stack5_, stack2_)
move(3, stack8_, stack5_)
move(5, stack3_, stack4_)
move(2, stack2_, stack1_)
move(9, stack8_, stack7_)
move(1, stack1_, stack8_)
move(6, stack5_, stack2_)
move(4, stack2_, stack8_)
move(4, stack7_, stack1_)
move(1, stack2_, stack6_)
move(5, stack1_, stack6_)
move(1, stack8_, stack2_)
move(1, stack2_, stack9_)
move(13, stack6_, stack5_)
move(2, stack7_, stack2_)
move(1, stack8_, stack7_)
move(4, stack4_, stack7_)
move(1, stack4_, stack1_)
move(4, stack8_, stack4_)
move(6, stack5_, stack9_)
move(2, stack1_, stack4_)
move(1, stack8_, stack6_)
move(11,stack9_, stack5_)
move(1, stack7_, stack8_)
move(1, stack8_, stack1_)
move(1, stack1_, stack3_)
move(6, stack4_, stack8_)
move(1, stack8_, stack4_)
move(1, stack1_, stack6_)
move(6, stack9_, stack7_)
move(1, stack4_, stack5_)
move(3, stack2_, stack1_)
move(1, stack8_, stack2_)
move(1, stack3_, stack2_)
move(20, stack5_, stack6_)
move(3, stack1_, stack6_)
move(2, stack2_, stack9_)
move(3, stack8_, stack3_)
move(5, stack3_, stack8_)
move(1, stack1_, stack6_)
move(2, stack8_, stack9_)
move(7, stack9_, stack5_)
move(3, stack5_, stack4_)
move(3, stack8_, stack3_)
move(9, stack7_, stack9_)
move(1, stack8_, stack5_)
move(7, stack7_, stack9_)
move(2, stack5_, stack2_)
move(9, stack9_, stack2_)
move(1, stack7_, stack3_)
move(2, stack9_, stack1_)
move(2, stack5_, stack9_)
move(2, stack1_, stack4_)
move(2, stack3_, stack7_)
move(18, stack6_, stack7_)
move(7, stack9_, stack1_)
move(7, stack6_, stack8_)
move(4, stack4_, stack9_)
move(4, stack8_, stack3_)
move(2, stack8_, stack2_)
move(1, stack8_, stack5_)
move(1, stack4_, stack7_)
move(1, stack5_, stack1_)
move(2, stack9_, stack3_)
move(12, stack2_, stack5_)
move(6, stack5_, stack6_)
move(5, stack7_, stack2_)
move(3, stack6_, stack4_)
move(1, stack4_, stack7_)
move(1, stack4_, stack1_)
move(2, stack5_, stack8_)
move(1, stack8_, stack2_)
move(2, stack9_, stack7_)
move(8, stack1_, stack8_)
move(11, stack7_, stack1_)
move(5, stack8_, stack2_)
move(7, stack7_, stack5_)
move(1, stack9_, stack4_)
move(1, stack7_, stack5_)
move(7, stack5_, stack7_)
move(2, stack6_, stack1_)
move(1, stack8_, stack2_)
move(12, stack1_, stack7_)
move(2, stack1_, stack2_)
move(3, stack8_, stack5_)
move(3, stack5_, stack2_)
move(8, stack7_, stack3_)
move(1, stack3_, stack1_)
move(3, stack6_, stack4_)
move(4, stack5_, stack6_)
move(14, stack2_, stack9_)
move(3, stack6_, stack9_)
move(3, stack4_, stack2_)
move(1, stack1_, stack7_)
move(1, stack7_, stack1_)
move(3, stack3_, stack5_)
move(8, stack7_, stack4_)
move(1, stack5_, stack9_)
move(3, stack2_, stack4_)
move(1, stack3_, stack4_)
move(4, stack2_, stack6_)
move(2, stack6_, stack7_)
move(3, stack5_, stack4_)
move(16, stack4_, stack1_)
move(7, stack9_, stack8_)
move(1, stack5_, stack1_)
move(3, stack7_, stack9_)
move(3, stack9_, stack4_)
move(7, stack1_, stack7_)
move(6, stack7_, stack1_)
move(5, stack3_, stack1_)
move(11, stack9_, stack2_)
move(3, stack4_, stack6_)
move(9, stack2_, stack8_)
move(6, stack3_, stack5_)
move(2, stack8_, stack6_)
move(5, stack5_, stack3_)
move(2, stack7_, stack1_)
move(3, stack3_, stack9_)
move(1, stack2_, stack4_)
move(1, stack5_, stack1_)
move(13, stack1_, stack2_)
move(5, stack8_, stack6_)
move(2, stack3_, stack9_)
move(2, stack4_, stack7_)
move(5, stack6_, stack9_)
move(7, stack9_, stack1_)
move(3, stack7_, stack2_)
move(6, stack8_, stack6_)
move(5, stack6_, stack2_)
move(2, stack8_, stack3_)
move(2, stack9_, stack4_)
move(6, stack2_, stack5_)
move(1, stack3_, stack7_)

# print the last letter of each stack on one line
print(stack1_[-1], stack2_[-1], stack3_[-1], stack4_[-1], stack5_[-1], stack6_[-1], stack7_[-1], stack8_[-1], stack9_[-1], sep='')


