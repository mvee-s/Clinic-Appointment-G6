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

def show_menu():
   
    print("1. Add patient")
    print("2. remove patient")
    print("3. edit patient")
    print("4. Show patient")
    print("5. Exit")

    choice = int(input("Enter number: "))

    match choice:
        case 1:
            add_patient(choice)
        case 2:
            remove_patient(choice)
        case 3:
            edit_patient(choice)
        case 4:
            show_patient()
        case 5:
            print("Exiting...")
            exit()
        case _:
            print("Invalid choice")

if __name__ == "__main__":
    show_menu()