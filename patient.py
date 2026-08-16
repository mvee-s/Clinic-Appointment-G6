patient_names = [] 

def add_patient(patient_name):
    patient_name = input("Add patient name: ") 
    patient_names.append(patient_name) 
    print("Patient added successfully") 

def remove_patient(patient_number): 
    show_patient()
    patient_number = int(input("Enter patient number to remove: ")) 

    if patient_number > 0 and patient_number <= len(patient_names): 
        patient_names.pop(patient_number - 1) 
        print("Patient removed successfully") 

def edit_patient(patient_number):
    show_patient() 
    
    patient_number = int(input("Enter patient number to edit: ")) 

    if patient_number > 0 and patient_number <= len(patient_names): 
        new_name = input("Enter new name: ") 
        patient_names[patient_number - 1] = new_name 
        print("Patient name updated successfully") 
    else:
        print("Invalid patient number") 

def show_patient():
    if len(patient_names) == 0: 
        print("No patients found")
    else: 
        for x, name in enumerate(patient_names):
            print(f"{x+1}: {name}")

def start_program():
    isRunning = True
    while isRunning:
        print("1. Add patient")
        print("2. remove patient")
        print("3. edit patient")
        print("4. Show patient")
        choice = int(input("Enter number: "))

        if choice < 1 or choice > 4:
            print("invalid choice")
        elif choice == 1:
            add_patient(choice)
        elif choice == 2:
            remove_patient(choice)
        elif choice == 3:
            edit_patient(choice)
        elif choice == 4:
            show_patient()

start_program()