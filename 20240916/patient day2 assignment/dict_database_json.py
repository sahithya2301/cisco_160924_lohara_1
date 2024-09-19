#1. class Patient {id, name}
class Patient:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()
#2. patients[]
patients = {}

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patient.id]=patient
#4. patient_remove(id)
def patient_remove(id):
    global patients
    patient=patient.get(id)
    if(patient==None):
        print(f'No such id {id}')
        return
    if input('Are you sure you want to delete? yes/no').lower()=='yes':
        del patients[id]
        print('Patient deleted successfully')
        #end if 
    #end for 

#5. patient_display()
def patient_display():
    global patients
    for i in patients:
        print(patients[i])
def patient_display_byId(id):
    global patients
    for patient in patients:
        if(patient.id==id):
            print (patient)
    print("No such Id found")
def patient_Update(id):
    global patients
    patient=patient.get(id)
    if patient==None:
        print(f'No such id {id}')
        return
    name=input('Enter the name you want to update to')
    patient.name=name
    print('updated successfully')

def readFile():
    with open("Patients_dict.json",'w') as db:
         db.write(f'List of patients{patients}')
    print("written into the file")
#6. menu 
def menu():
    choice = int(input('''1-add patient
2-delete patient by id
3-display all patients
4-display by id
5-update name by id
6-write into file
7-end                       
your choice:'''))
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('Enter patient name:')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to delete:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice==4:
        id=input("enter patient id")
        patient_display_byId(id)
    elif choice==5:
        id=input("enter patient id")
        patient_Update(id)
    elif choice==6:
        readFile()
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
