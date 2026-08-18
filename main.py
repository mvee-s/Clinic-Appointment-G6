from patient import patient_menu
from doctor import doctor_menu

def summary():
    print("\nClinic Management Summary:")
    print("==========================")
    print("1. View Patient")
    print("2. View Doctor")
    print("3. View Schedule")  
    
isRunning = True
while isRunning:
    
    print("====================")
    print(" Clinic Management")
    print("====================")
    
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Schedule Management")
    print("4. Exit")
    
    try:
        choice = int(input("Enter number: "))
    
        match choice:
            case 1:
                patient_menu()
            case 2:
                doctor_menu()
            case 3: 
                summary()
            case 4:
                isRunning = False
                print("Exiting...")
            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please enter a number.")