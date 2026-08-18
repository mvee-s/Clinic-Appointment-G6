doctors = []

def add_doctor():
    name = input("Enter new Doctor name: ")
    specialization = input("Enter Specialization: ")

    doctor = {
        "name" : name,
        "specialization" : specialization,
        "schedule" : []
    }

    print("ADD DOCTOR SCHEDULE")
    
    while True:
        day = input("Enter day: ")
        time = input("Enter time: ")

        schedule = {
            "day": day,
            "time": time,
            "available": True
        }
        
        doctor["schedule"].append(schedule)

        print("Schedule added successfully")

        another = input("Do you want another schedule? (Y/N): ")

        if another.upper() != "Y":
            break

    doctors.append(doctor) 

def view_doctors():
    if len(doctors) == 0:
        print("No doctors found.")
        return

    for i, doctor in enumerate(doctors, start=1):
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

                print(f" - {schedule['day']} | {schedule['time']} | {status}")
                

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

def edit_doctor():
    view_doctors()

    if len(doctors) == 0:
        return

    choice = int(input("Select doctor number to edit: "))

    if 1 <= choice <= len(doctors):
        doctor = doctors[choice - 1]

        while True:
            print("[1. Edit Name]")
            print("[2. Edit Specialization]")
            print("[3. Edit Schedule]")
            print("[4. Back]")

            edit_choice = input("What do you want to edit? ")

            if edit_choice == "1":
                new_name = input("Enter updated name: ")

                if new_name != "":
                    doctor["name"] = new_name
                    print("Doctor name updated successfully.")
                else:
                    print("Name cannot be empty.")

            elif edit_choice == "2":
                new_specialization = input("Enter updated Specialization: ")

                if new_specialization != "":
                        doctor["specialization"] = new_specialization
                        print("\nSpecialization updated successfully.")
                else:
                    print("\nSpecialization cannot be empty.")

            elif edit_choice == "3":
                if len(doctor["schedule"]) == 0:
                    print("\nNo schedule found for this doctor.")
                
                else:
                    print(f"\n===== SCHEDULE OF DR. {doctor['name'].upper()} =====")
                    

                    for i, schedule in enumerate(doctor["schedule"], start=1):
                        status = "Available" if schedule["available"] else "Booked"

                        print(
                            f"{i}. {schedule['day']} - "
                            f"{schedule['time']} - {status}"
                        )

                    schedule_choice = int(
                        input("\nEnter schedule number to edit: ")
                    )

                    if 1 <= schedule_choice <= len(doctor["schedule"]):
                        schedule = doctor["schedule"][schedule_choice - 1]

                        print("\nWhat do you want to edit?")
                        print("[1. Day]")
                        print("[2. Time]")
                        print("[3. Availability]")

                        schedule_edit = input("\nEnter choice: ")

                        if schedule_edit == "1":
                            new_day = input("Enter new day: ")

                            if new_day != "":
                                schedule["day"] = new_day
                                print("\nDay updated successfully.")
                            else:
                                print("\nDay cannot be empty.")

                        elif schedule_edit == "2":
                            new_time = input("Enter new time: ")

                            if new_time != "":
                                schedule["time"] = new_time
                                print("\nTime updated successfully.")
                            else:
                                print("\nTime cannot be empty.")

                        elif schedule_edit == "3":
                            print("\n[1. Available]")
                            print("[2. Booked]")

                            availability = input(
                                "Enter availability: "
                            )

                            if availability == "1":
                                schedule["available"] = True
                                print("\nSchedule is now Available.")

                            elif availability == "2":
                                schedule["available"] = False
                                print("\nSchedule is now Booked.")

                            else:
                                print("\nInvalid choice.")

                        else:
                            print("\nInvalid choice.")

                    else:
                        print("\nInvalid schedule choice.")

            elif edit_choice == "4":
                break

            else:
                print("\nInvalid choice.")

    else:
        print("\nInvalid doctor choice.")

def add_schedule():
    view_doctors()

    if len(doctors) == 0:
        return

    choice = int(
        input("Enter doctor number to add schedule: ")
    )

    if 1 <= choice <= len(doctors):

        doctor = doctors[choice - 1]

        day = input(
            "Enter day (e.g. Monday): "
        )

        time = input(
            "Enter time (e.g. 9:00 AM): "
        )

        schedule = {
            "day": day,
            "time": time,
            "available": True
        }

        doctor["schedule"].append(schedule)

        print(
            f"\nSchedule added successfully for "
            f"Dr. {doctor['name']}."
        )

    else:
        print("\nInvalid Choice.")

def menu_doctor():

    while True:
        print("\n==========LIST OF DOCTORS==========")
        view_doctors()

        print("\n==========DOCTOR MENU==========")
        print("[1. View Doctors]")
        print("[2. Add Doctors]")
        print("[3. Edit Doctors]")
        print("[4. Delete Doctors]")
        print("[5. Exit]")

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
            print("======================")
            print("List of Doctors")
            break

        else:
            print("Invalid choice.")

menu_doctor()


print("\nDoctors: ")

for doctor in doctors:
    print(f"Doctor {doctor['name']}")
    print(f"Specialization: {doctor['specialization']}")



