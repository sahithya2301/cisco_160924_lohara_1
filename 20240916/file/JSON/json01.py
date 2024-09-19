import json
patients = [
    {'id' : 101, 'name' : 'sahithya'},
    {'id' :102, 'name' : 'Akhila'}
]
patients_str = json.dumps(patients)
print(patients,patients_str)
with open('patients_data.json', 'w') as patients_db:
    json.dump(patients,patients_db)

patients_list = json.loads(patients_str)
print(patients_list,type(patients_list))

with open('patients_data.json','r') as patients_db:
    patients_list1 = json.loads(patients_str)
    print(patients_list1,type(patients_list))