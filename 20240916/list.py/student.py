#takes alist of student names as input
names_list=input("enter the names of students").split()
#convert list to a set 
names_set = set(names_list)

#convert the set to a frozenset
names_fset = frozenset(names_set)
#dictionary of name length
names_dict = {name:len(name) for name in names_fset}
print(f'Original list: {names_list}')
print(f'set (no duplicates): {names_set}')
print(f'Frozen set: {names_fset}')
print(f'Dictionary of name length: {names_dict}')
import json
with open("q02_data.json",'w') as names_db:
    json.dump(names_dict, names_db)
print('Dictionary written to JSON file.')  
with open("q02_data.json",'r') as names_db: 
    names_dict2 = json.load(names_db) 
    print(f'Reading from JSON file....\n{names_dict2}')
