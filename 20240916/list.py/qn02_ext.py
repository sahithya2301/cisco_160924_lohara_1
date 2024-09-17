import json
with open("q02_data.json",'w') as names_db:
    json.dump(names_dict, names_db)
print('Dictionary written to JSON file.')  
with open("q02_data.json",'r') as names_db: 
    names_dict2 = json.load(names_db) 
    print(f'Reading from JSON file....\n{names_dict2}')