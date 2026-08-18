import patient 
import doctor

isRunning = True
while isRunning:
    
    print("====================")
    print(" Clinic Management")
    print("====================")
    
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Exit")
    
    try:
        choice = int(input("Enter number: "))

        match choice:
            case 1:
                patient.patient_menu()
            case 2:
                doctor.doctor_menu()
            case 3:
                isRunning = False
                print("Exiting...")
            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please enter a number.")