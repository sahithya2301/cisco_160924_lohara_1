class Patient:
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()        
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
                print('patients updated successfully')
            return  
    print(f'No such id {id}')                 
def menu():
    choice = int(input('''1-add patient
2- delete patient by id
3- display all patients
4- read patient by id
5- update patient by id                                              
7-end
your choice.'''))
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('Enter patient name:') 
        patient_add(id, name) 
    elif choice == 2:
        id = int(input('Enter patient id to delete:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice == 4:
        id = int(input('Enter patient id:'))
        patient_display_byid(id)
            
    elif choice == 5:
        id = int(input('Enter patient id:'))
        patient_update(id)
    elif choice == 7:
        pass 
    else:
       print('Invalid menu')
    return choice
#7. menus 
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')
#8. driver program
menus()    

    

# Function to display all patients

   

# Main program loop
