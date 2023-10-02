dict = {'item1':{'item11':11, 'item12':12, 'dir11':{'item111':111}}, 
        'item2':{'item21': 21, 'dir21':{'item211':211, 'item212':212}}, 
        'item3':{'item31':31, 'dir31':{'item311':311, 'item312':312}, 'dir32':{'item321':321, 'item322':322}}}

dict_copy = dict

def down_dir(*keys, current_dir, new_dir):


    for key in keys:

        print(type(current_dir))

        current_dir = current_dir[key]

    dict_copy = current_dir

    dict_copy[new_dir] = {'itemnew':True}

    print(dict_copy)
    print(dict)


down_dir('item3', 'dir31', current_dir=dict_copy, new_dir='dirnew')