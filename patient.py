patient_names = []

def add_patient(patient_name):
    patient_name = input("Add patient name: ")
    patient_names.append(patient_name)
    print("Patient added successfully")

def remove_patient(patient_number):
    patient_names.pop()

def edit_patient(patient_number):
    patient_names[patient_number] = input("Enter new patient name: ")
    print("Patient updated successfully")

def show_patient():
    if len(patient_names) == 0:
        print("No patients found")
    else:
        for x in patient_names:
            print(x)

def start_program():
    isRunning = True
    while isRunning:
        print("1. Add patient")
        print("2. remove patient")
        print("3. edit patient")
        print("4. Show patient")
        choice = int(input("Enter number: "))

        if choice < 0 or choice > 4:
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