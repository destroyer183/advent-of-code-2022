

class Stack:

    stacks = []

    def __init__(self, stack_num, stack_contents) -> None:

        self.stack_num = stack_num
        self.stack_contents = stack_contents

        print(f"stack num: {stack_num}")
        print(f"stack contents: {stack_contents}")

        Stack.add_stack(self)
        
        pass



    def build_stack(self):

        pass



    @classmethod
    def move_item(cls, start: int, count: int, end: int):

        for i in range(count):

            cls.stacks[end - 1].stack_contents.append(cls.stacks[start - 1].stack_contents.pop())

        for i in range(9):

            print(f"Stack {cls.stacks[i].stack_num}: {cls.stacks[i].stack_contents}")

        print('')


    
    @classmethod
    def add_stack(cls, stack):

        cls.stacks.append(stack)



    @classmethod
    def get_last_item(cls):

        print(f"output: {cls.stacks[0].stack_contents[-1]}{cls.stacks[1].stack_contents[-1]}{cls.stacks[2].stack_contents[-1]}{cls.stacks[3].stack_contents[-1]}{cls.stacks[4].stack_contents[-1]}{cls.stacks[5].stack_contents[-1]}{cls.stacks[6].stack_contents[-1]}{cls.stacks[7].stack_contents[-1]}{cls.stacks[8].stack_contents[-1]}")
   



with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        print(x)

        x = x.split(" ")

        if x == '': continue

        if x[0] in '1234567890':

            Stack(x[0], x[1:len(x)])


        else:

            Stack.move_item(int(x[3]), int(x[1]), int(x[5]))

Stack.get_last_item()