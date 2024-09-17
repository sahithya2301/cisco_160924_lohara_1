from patient import Patient
patients = []


# Function to add a patient
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)

# Function to remove a patient
def patient_remove(name):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no?').lower() == 'yes':
                patients.remove(patient)
                print('patients deleted successfully')
            return
        #end if
    #end for
    print(f'No such id (id)')   
         
def patient_display():
    global patients
    for patient in patients:
        print(patient)
def patient_display_byid(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            return
    print('Invalid id')
def patient_update(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient) 
            if input('Are you sure to update(yes/no?').lower() == 'yes':
                patients.remove(patient)
                print('patients upadted successfully')
            return  
    print(f'No such id {id}')     