from patient import Patient
patients = {}


# Function to add a patient
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patient.id]=patient
    print('Patient created successfully')

# Function to remove a patient
def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient ==  None:
        print(f'No such id {id}')
        return
    print(patient)
    if input('Are you sure to delete(yes/no?').lower() == 'yes':
        del patients[id]
       # patients.remove(patient)
        print('patients deleted successfully') 
         
def patient_display():
    global patients
    for id in patients:
        print(patients[id])

def patient_display_byid(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    
def patient_update(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}') 
        return
    print(patient)
    name = input(f'Enter new name({patient.name})')
    patient.name = name 
    print('Patient updated successfully')