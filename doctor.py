doctor_names = [] 

def add_doctor():
    doctor_name = input("Add doctor name: ") 
    doctor_names.append(doctor_name) 
    print(f"doctor {doctor_name} added successfully") 

def remove_doctor(): 
    if len(doctor_names) == 0:
        print("No doctors to remove")
        return
    show_doctor()
    doctor_number = int(input("Enter doctor number to remove: ")) 

    if doctor_number > 0 and doctor_number <= len(doctor_names): 
        doctor_names.pop(doctor_number - 1) 
        print(f"doctor removed successfully") 

def edit_doctor():
    if len(doctor_names) == 0:
        print("No doctors to edit")
        return
    
    show_doctor() 
    doctor_number = int(input("Enter doctor number to edit: ")) 

    if doctor_number > 0 and doctor_number <= len(doctor_names): 
        new_name = input("Enter new name: ") 
        doctor_names[doctor_number - 1] = new_name 
        print(f"doctor updated successfully") 
    else:
        print("Invalid doctor number") 

def show_doctor():
    if len(doctor_names) == 0: 
        print("No doctors found")
    else: 
        print("====================")
        print("   doctor List:")
        for x, name in enumerate(doctor_names):
            print(f"{x+1}: {name}")
        print("====================")

def doctor_menu():
   
    print("")
    print("====================")
    print(" doctor Management")
    print("====================")
    print("1. Show doctor")
    print("2. Add doctor")
    print("3. Edit doctor")
    print("4. Remove doctor")
    print("5. Exit")
    
    try:

        choice = int(input("Enter number: "))

        match choice:
            case 1:
                show_doctor()
            case 2:
                add_doctor()
            case 3:
                edit_doctor()
            case 4:
                remove_doctor()
            case 5:
                print("Exiting...")
                exit()
            case _:
                print("Invalid choice")
    except ValueError:
        print("Invalid choice")


if __name__ == "__main__":
    show_menu()