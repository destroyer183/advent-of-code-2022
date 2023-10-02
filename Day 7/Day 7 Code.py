
# use a dictionary, probably nested dicts, with a class for each file

# maybe store the current dir like a computer, and then use .split('/') to separate it into iterable indicies.


class Dir:

    base_dir = {}
    current_dir = base_dir
    current_dir_hist = {}
    parent_dir = current_dir

    def __init__(self, name, dir = None, size = 0) -> None:

        self.name = name
        self.dir = dir
        self.size = size

        if self not in Dir.current_dir:

            Dir.new_dir(self)


    
    @classmethod
    def new_dir(cls, name): 

        cls.current_dir[name] = {}



    @classmethod
    def list(cls, location, type):

        listnames = {}
        list = {}

        for item in location:

            list[item] = item

            listnames[item.name] = item



        if type:

            return listnames
        

        
        if not type:

            return list
        


    @classmethod
    def change_dir(cls, dir, type):

        if type == 'base dir':

            cls.current_dir = cls.base_dir



        elif type == 'set dir':

            cls.current_dir = cls.base_dir

            for key in dir:

                cls.current_dir = cls.current_dir[key]



    @classmethod
    def add_file(cls, file):

        cls.current_dir[file] = file

        cls.current_dir = cls.base_dir

        for key in file.dir:

            key.size += int(file.size)

            cls.current_dir = cls.current_dir[key]


            
class File(Dir):

    def __init__(self, name, dir, size) -> None:

        super().__init__(name, dir)
        self.size = size



with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        print(f"line: {x}")

        x = x.split(" ")

        if x[0] == '$':

            if x[1] == 'ls':

                pass



            elif x[2] == '/':

                Dir.change_dir([], type='base dir')



            elif x[2] in Dir.list(Dir.current_dir, type=True):

                if x[2] not in Dir.list(Dir.current_dir, type=True):

                    Dir(x[2], Dir.current_dir_hist, Dir.parent_dir)

                Dir.current_dir_hist[Dir.list(Dir.current_dir, type=True)[x[2]]] = Dir.list(Dir.current_dir, type=True)[x[2]]

                Dir.change_dir(Dir.current_dir_hist, type='set dir')



            elif x[2] == '..':

                Dir.current_dir_hist.popitem()

                Dir.change_dir(Dir.current_dir_hist, type='set dir')



        elif x[0] == 'dir':

            if x[1] not in Dir.list(Dir.current_dir, type=True):

                Dir(x[1], Dir.current_dir_hist, Dir.parent_dir)




        else:


            if x[1] not in Dir.list(Dir.current_dir, type=True):

                Dir.add_file(File(x[1], Dir.current_dir_hist, x[0]))




def get_all_keys(d):

    for key, value in d.items():

        yield key

        if isinstance(value, dict):

            yield from get_all_keys(value)

                

total_size = 0

for x in get_all_keys(Dir.base_dir):

    if int(x.size) <= 100000 and type(x) == Dir:

        total_size += int(x.size)


print(f"total size: {total_size}")