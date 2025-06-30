habit_log = {}

def add_habit():
    habit_name = input("Enter your habit: ").lower()
    progress_status = input("Are you done: Yes, no?").lower()

    habit_log[habit_name] = progress_status

    motivate = lambda progress_status:(
        "Done! You just conquered another one." if progress_status == "yes"
        else "Keep going! Every step forward counts." if progress_status == "no"
        else "Oops! invalid choice "
    )
    print(f"✅ Habit logged! Your future self will thank you")


def view_all():
    for habit_name, progress_status in habit_log.items():
        print(f"{habit_name} -> {progress_status}")

def check_habit():
    search = input("Enter habit name: ")
    result = habit_log.get(search)

    if result:
        print(f"{result} -> {search}")
    else:
        print("Oops! That habit hasn't been added yet")

def view_habits():
    for habit_name in habit_log.keys():
        print(f"{habit_name}")


while True:
    print("1. Add a new habit")
    print("2. View all habits & status")
    print("3. Check a specific habit")
    print("4. View only habit names")
    print("5. Exit")

    choice = input("Please enter your choice: ")

    match choice:
        case "1":
            add_habit()

        case "2":
            view_all()

        case "3":
            check_habit()

        case "4":
            view_habits()

        case "5":
            print("Exiting...Keep up the good work! ")
            break

        case _:
            print("Invalid choice try again")