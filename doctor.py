doctors_names = []

def add_doctor(doctors_name):
    doctors_names.append(doctors_name)

    for doctor in doctors_names:
        print(f"Doctor: {doctor}")

new_doctor = add_doctor(input("Enter new doctor name: "))

