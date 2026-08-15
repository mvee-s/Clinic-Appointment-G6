patient_names = []

def add_patient(patient_name):
    patient_name = add_patient(input("Add patient name: "))
    patient_names.append(patient_name)
    for x in patient_names:
        print(x)

def remove_patient(patient_number):
    patient_names.pop()

# def edit_patient(patient_number):


# def show_patient():


def start_program():
    isRunning = True:
        print("1. Show patient")
        print("2. Show patient")
        print("3. Show patient")
        print("4. Show patient")
        choice = int(input("Enter number: "))

        if choice < 0 or choice > 4:
            print("invalid choice")
            
        



    
    







