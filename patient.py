patient_names = [] 

def add_patient():
    patient_name = input("Add patient name: ") 
    
    if patient_name.strip() == "": 
        print("Patient name cannot be empty") 
        return
    
    patient_names.append(patient_name) 
    print(f"Patient {patient_name} added successfully") 

def remove_patient(): 
    if len(patient_names) == 0:
        print("No patients to remove")
        return
    show_patient()
    patient_number = int(input("Enter patient number to remove: ")) 

    if patient_number > 0 and patient_number <= len(patient_names): 
        patient_names.pop(patient_number - 1) 
        print(f"Patient removed successfully") 

def edit_patient():
    if len(patient_names) == 0:
        print("No patients to edit")
        return
    
    show_patient() 
    patient_number = int(input("Enter patient number to edit: ")) 

    if patient_number > 0 and patient_number <= len(patient_names): 
        new_name = input("Enter new name: ") 
        if new_name.strip() == "": 
            print("Patient name cannot be empty") 
            return
        patient_names[patient_number - 1] = new_name 
        print(f"Patient updated successfully") 
    else:
        print("Invalid patient number") 

def show_patient():
    if len(patient_names) == 0: 
        print("No patients found")
    else: 
        print("====================")
        print("   Patient List:")
        for x, name in enumerate(patient_names):
            print(f"{x+1}: {name}")
        print("====================")

def patient_menu():
    while True:
        print("")
        print("====================")
        print(" Patient Management")
        print("====================")
        print("[1] Show patient")
        print("[2] Add patient")
        print("[3] Edit patient")
        print("[4] Remove patient")
        print("[5] Exit")
        
        try:

            choice = int(input("Enter number: "))

            match choice:
                case 1:
                    show_patient()
                case 2:
                    add_patient()
                case 3:
                    edit_patient()
                case 4:
                    remove_patient()
                case 5:
                    print("Exiting to patient menu...")
                    return
                case _:
                    print("Invalid choice")
        except ValueError:
            print("Invalid choice")


if __name__ == "__main__":
    patient_menu()