doctors = []

def add_doctor(name):
    doctors.append(name) 

add_doctor(input("Enter new Doctor name: "))

print("\nDoctors: ")
for doctor in doctors:
    print(f"Doctor {doctor}")



