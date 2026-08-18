doctors = []

def add_doctor():
    name = input("Enter new Doctor name: ")
    specialization = input("Enter Specialization: ")

    doctor = {
        "name" : name,
        "specialization" : specialization,
        "schedule" : []
    }
    doctors.append(doctor) 

def view_doctors():
    if len(doctors) == 0:
        print("No doctors found.")
        return

    for i, doctor in enumerate(doctors, start=1):
        print(f"{i}. Dr. {doctor['name']}")
        print(f"Specialization: {doctor['specialization']}")

def delete_doctor():
    view_doctors()

    if len(doctors) == 0:
        return

    choice = int(input("[Enter doctor number to delete: ]"))

    if 1 <= choice <= len(doctors):
        deleted = doctors.pop(choice - 1)
        print(f"\n{deleted['name']} has been deleted.")

    else:
        print("\nInvalid Choice.")


def menu_doctor():
    while True:
        print("[1. View Doctors]")
        print("[2. Add Doctors]")
        print("[3. Edit Doctors]")
        print("[4. Delete Doctors]")
        print("[5. Exit]")

        

add_doctor()

print("\nDoctors: ")

for doctor in doctors:
    print(f"Doctor {doctor['name']}")
    print(f"Specialization: {doctor['specialization']}")



