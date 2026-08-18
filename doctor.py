doctors = []

def get_valid_name(message):
    while True:
        name = input(message).strip()

        if name == "":
            print("Input cannot be empty.")

        elif not name.replace(" ", "").isalpha():
            print("Kindly enter letters only.")

        else:
            return name

def get_valid_specialization():
    while True:
        specialization = input("Enter Specialization: ").strip()

        if specialization == "":
            print("Specialization cannot be empty.")
        
        else:
            return specialization

def get_valid_day():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    while True:
        day = input("Enter (Monday - Sunday): ").strip().capitalize()

        if day in days:
            return day
        
        print("Invalid day. Please enter Monday - Sunday only.")

def get_valid_time(message):
    while True:
        time = input(message).strip()

        try:
            from datetime import datetime

            datetime.strptime(time, "%I:%M %p")
            return time.upper()

        except ValueError:
            print("\nInvalid Time. Follow 12-hour time format: (e.g. 9:00 AM)")

def get_valid_time_range():
    while True:
        start_time = get_valid_time("\nFollow 12-hour time format. \nEnter start time (e.g. 9:00 AM): ")

        end_time = get_valid_time("Enter end time (e.g. 5:00 PM): ")

        from datetime import datetime

        start = datetime.strptime(start_time, "%I:%M %p")
        end = datetime.strptime(end_time, "%I:%M %p")

        if end > start:
            return start_time, end_time

        print("\nEnd time must be later than start time.")
def get_valid_number(message, minimum, maximum):
    while True:
        try:
            choice = int(input(message))

            if minimum <= choice <= maximum:
                return choice

            print("\nInvalid choice.")

        except ValueError:
            print("\nKindly enter a number.")
            
def schedule_exists(doctor, day, start_time, end_time):
    for schedule in doctor["schedule"]:

        if schedule["day"] == day and schedule["start_time"] == start_time and schedule["end_time"] == end_time:
            return True
    return False

def add_doctor():
    name = get_valid_name("Enter new Doctor name: ")
    specialization = get_valid_specialization()

    doctor = {
        "name" : name,
        "specialization" : specialization,
        "schedule" : []
    }

    print("\n==========ADD DOCTOR SCHEDULE==========")
    
    while True:
        day = get_valid_day()

        start_time, end_time = get_valid_time_range()

        if schedule_exists(doctor, day, start_time, end_time):
            print("\n Schedule already exists.")
            continue

        schedule = {
            "day": day,
            "start_time": start_time,
            "end_time": end_time,     
            "available": True
        }
        
        doctor["schedule"].append(schedule)

        print("\nSchedule added successfully")

        another = input("\nDo you want another schedule? (Y/N): ")

        if another.upper() != "Y":
            break

    doctors.append(doctor) 

def view_doctors():
    if len(doctors) == 0:
        print("==========NO DOCTORS FOUND==========")
        return

    for i, doctor in enumerate(doctors, start=1):
        print("\n==========LIST OF DOCTORS==========")
        print(f"{i}. Dr. {doctor['name']}")
        print(f"Specialization: {doctor['specialization']}")

        if len(doctor["schedule"]) == 0:
            print("No schedule for this week.")

        else:
            print("Schedule: ")

            for schedule in doctor["schedule"]:
                status = ("Available"
                    if schedule["available"]
                    else "Booked"
                )

                print(f" - {schedule['day']} | {schedule['start_time']} - {schedule['end_time']} | {status}")
                

def delete_doctor():
    view_doctors()

    if len(doctors) == 0:
        return

    choice = get_valid_number("Enter Doctor number to delete: ", 1, len(doctors))

    deleted = doctors.pop(choice - 1)
    
    print(f"\n{deleted['name']} has been deleted.")

def edit_doctor():
    view_doctors()

    if len(doctors) == 0:
        return

    choice = get_valid_number("Enter Doctor number to edit: ", 1, len(doctors))

    doctor = doctors[choice - 1]

    while True:
        print("[1] Edit Name]")
        print("[2] Edit Specialization]")
        print("[3] Edit Schedule]")
        print("[4] Add Schedule]")
        print("[5] Back]")

        edit_choice = get_valid_number("What do you want to edit? ", 1, 5)

        if edit_choice == 1:
            new_name = get_valid_name("Enter updated name: ")

            doctor["name"] = new_name
            
            print("Doctor name updated successfully.")
            

        elif edit_choice == 2:
            new_specialization = get_valid_specialization()
            
            doctor["specialization"] = new_specialization

            print("\nSpecialization updated successfully.")
            

        elif edit_choice == 3:
            if len(doctor["schedule"]) == 0:
                print("\nNo schedule found for this doctor.")
            
            else:
                print(f"\n===== SCHEDULE OF DR. {doctor['name'].upper()} =====")
                

                for i, schedule in enumerate(doctor["schedule"], start=1):
                    status = "Available" if schedule["available"] else "Booked"

                    print(f"{i}. {schedule['day']} - {schedule['start_time']} - {schedule['end_time']} {status}")

                schedule_choice = get_valid_number("\nEnter schedule number to edit: ", 1, len(doctor["schedule"]))

                
                schedule = doctor["schedule"][schedule_choice - 1]

                print("\nWhat do you want to edit?")
                print("[1] Day]")
                print("[2] Start Time]")
                print("[3] End Time]")
                print("[4] Availability]")

                schedule_edit = get_valid_number("\nEnter choice: ", 1, 4)

                if schedule_edit == 1:
                    new_day = get_valid_day()
                    
                    schedule["day"] = new_day
                    print("\nDay updated successfully.")
                    

                elif schedule_edit == 2:
                    new_start_time = get_valid_time("\nFollow 12-hour time format. \nEnter new start time (e.g. 9:00 AM)")
                
                    schedule["start_time"] = new_start_time
                    print("\nStart Time updated successfully.")
                
                elif schedule_edit == 3:
                    new_end_time = get_valid_time("\nFollow 12-hour time format. \nEnter new end time (e.g. 5:00 PM)")
                
                    schedule["end_time"] = new_end_time
                    print("\nEnd Time updated successfully.")
                    

                elif schedule_edit == 4:
                    print("\n[1] Available]")
                    print("[2] Booked]")

                    availability = get_valid_number("Enter availability: ", 1, 2)

                    if availability == 1:
                        schedule["available"] = True
                        print("\nSchedule is now Available.")

                    elif availability == 2:
                        schedule["available"] = False
                        print("\nSchedule is now Booked.")

        elif edit_choice == 4:
            day = get_valid_day()

            start_time, end_time = get_valid_time_range()
            

            if schedule_exists(doctor, day, start_time, end_time):
                print("\nSchedule already exists.")
                continue
            schedule = {
                "day": day,
                "start_time": start_time,
                "end_time": end_time,
                "available": True
            }

            doctor["schedule"].append(schedule)

            print(f"\nSchedule added successfully for Dr. {doctor['name']}.")


        elif edit_choice == 5:
            break

        else:
            print("\nInvalid choice.")

    


def doctor_menu():

    while True:
        print("\n==========DOCTOR MENU==========")
        print("[1] View Doctors]")
        print("[2] Add Doctor]")
        print("[3] Edit Doctor]")
        print("[4] Delete Doctor]")
        print("[5] End]")

        choice = input("\nEnter choice: ")

        if choice == "1":
            view_doctors()

        elif choice == "2":
            add_doctor()
        
        elif choice == "3":
            edit_doctor()

        elif choice == "4":
            delete_doctor()

        elif choice == "5":
            for i, doctor in enumerate(doctors, start=1):
                print("==========LIST OF DOCTORS==========")
                print(f"{i}. Dr. {doctor['name']}")

            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    doctor_menu()




