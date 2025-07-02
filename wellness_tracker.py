sleep_log = {}
meal_log = {}
exercise_log = {}

while True:
    print("1. Log sleep hours")
    print("2. Log meal for the day")
    print("3. Log exercise")
    print("4. View all wellness logs")
    print("5. Search log by category")
    print("6. Compare exercise routines with a friend")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    def sleep_hours():
        day = input("Enter day(e.g., Monday): ").lower()
        hours = int(input("Hours "))

        sleep_log[day] = hours

        sleep_motivation = lambda hours:(
            "Good amount of sleep" if hours >=6 and hours <= 8
            else "Get ample sleep" if hours < 6 
            else "Too much sleep" if hours > 8
            else "Login sleeping time"
        )
        print(f"✅ Logged. {sleep_motivation (hours)}")

    def meal_time():
        time = input("Period (breakfast/lunch/dinner)? ").lower()
        food = input("Food: ").lower()

        meal_log[time] = food

        meal_motivation = lambda time:(
            "Started your day well" if time == "breakfast"
            else "Fuel your afternoon" if time == "lunch"
            else "End the day with a healthy meal" if time == "dinner"
            else "Oops! try again"
        )
        print(f"✅ {time} logged!  {meal_motivation(time)}")

    def exercise_time():
        exercise = input("What exercise: ").lower()
        intensity = input("(low, medium, high)? ").lower()

        exercise_log[exercise] = intensity

        exercise_motivation = lambda intensity:(
            "Feel the burn, champion! 💪" if intensity == "high"
            else " Keep working on " if intensity == "medium"
            else "Keeping fit is essential...Let's gooo  💪"  if intensity == "low"          
            else "Invalid input mate! 😊"
        )
        print(f"✅ Logged. {exercise_motivation(intensity)}")

    def all_logs():
        print("\n--- Wellness Logs ---")
        print("\n 🛏️ Sleep Log:")
        for day, hours in sleep_log.items():
            print(f"{day}->{hours}")

        print("\n🍴 Meal Log:")
        for time, food in meal_log.items():
            print(f"{time}->{food}")

        print("\n🏃 Exercise Log:")
        for exercise, intensity in exercise_log.items():
            print(f"{exercise}->{intensity}")


    def search_logs():
        search_in = input("(sleep/meal/exercise): ").lower()
        search_key = input("Enter search key (e.g., Monday or lunch or push-ups): ").lower()

        if search_in == "sleep":
            result = sleep_log.get(search_key)
            if result:
                print(f"🛏️ You slept {result} hrs on {search_key}")
            else:
                print("Day not found!")

        elif search_in == "meal":
            result = meal_log.get(search_key)
            if result:
                print(f"🍴 For {search_key}, you ate {result}")
            else:
                print("Meal time not found!")

        elif search_in == "exercise":
            result = exercise_log.get(search_key)
            if result:
                print(f"🏃 You did {search_key} with {result} intensity")
            else:
                print("Exercise not found!")

        else:
            print("Invalid category!")

    def activities_log():
        own_exercise = input("Enter your exercise: ").split(",")
        friends_exercise = input("Enter friend's exercise: ").split(",")

        own_activity = set(own_exercise)
        friends_activity = set(friends_exercise)

        all_activity = own_activity.union(friends_activity)
        print(all_activity)

        mutual_activity = own_activity.intersection(friends_activity)
        print(mutual_activity)

        unique_activity = own_activity.difference(friends_activity)
        print(unique_activity)

    match choice:
        case 1:
            sleep_hours()
        
        case 2:
            meal_time()

        case 3:
            exercise_time()

        case 4:
            all_logs()

        case 5:
            search_logs()

        case 6:
            activities_log()

        case 7:
            print("Exiting Wellness Planner... Stay consistent and keep growing! 🌱")
            break

        case _:
            print("Opps! Invalid choice...try again")

            # All other parts worked well other than the previous comment

            