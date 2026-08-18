import patient
import doctor

def summary():
    while True:
        print("\n==========SUMMARY==========")
        print("[1] View Patient]")
        print("[2] View Doctor]")
        print("[3] Back]")
  
        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                patient.show_patient()
            case 2:
                doctor.view_doctors()
            case 3:
                return
            case _:
                print("Invalid choice. Please try again.")


isRunning = True
while isRunning:

    print("====================")
    print(" Clinic Management")
    print("====================")

    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Summary")
    print("4. Exit")

    try:
        choice = int(input("Enter number: "))

        match choice:
            case 1:
                patient.patient_menu()
            case 2:
                doctor.doctor_menu()
            case 3:
                summary()
            case 4:
                isRunning = False
                print("Exiting...")
            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please enter a number.")