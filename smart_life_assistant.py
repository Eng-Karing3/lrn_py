smart_life = {}
mood_log = {}
study_log = {}
expenses_log = {}



print("\n Welcome to Smart Life Assistant 💡")

while True:
    print("1. Log a new task")
    print("2. Add mood entry")
    print("3. Record study session")
    print("4. Add expense")
    print("5. Compare activities with a friend")
    print("6. View all logs")
    print("7. Search specific log")
    print("8. Exit")
    
    choice = int(input("Enter choice: "))

    def new_task():
        
        task_name = input("Task: ").lower()
        priority = input("Priority -> high , medium low").lower()
        time_bound = input("Time-bound: yes or no").lower()

        smart_life[task_name] = priority, time_bound

        reminder = lambda priority:(
            "start with this" if priority == "high"
            else "you can work on this" if priority == "medium"
            else "This can wait until later" if priority == "low"
            else "Oops! Invalid choice"
        )
        print(f"Reminder: {task_name} is a {priority} task that {reminder(priority)}")

    def mood_entry():

        mood = input("Mood: ").lower()
        time_of_day = input("Time of Day: ").lower()

        mood_log[mood] = time_of_day

        mood_motivation = lambda mood:(
            "Keep smiling 😊" if mood == "happy"
            else "Cheer up mate 🙂" if mood == "sad"
            else "Relax..Just relax 😌" if mood == "Stressed" 
            else "Oops! Not familiar try again"
        )
        print(f"Mood logged! {mood_motivation(mood)}")

    def study_sessions():
        subject = input("Subject: ").lower()
        hours =  int(input("Hours"))

        study_log[subject] = hours

        study_motivation = lambda hours:(
        "Great focus"  if hours  <= 3 and hours >= 2
        else "Too much for studying" if hours > 3
        else "Little time for studying " if hours < 1
        else "Enter hours"
        )
        print(f"Study session recorded. {study_motivation(subject)}!")

    def expenses():

        category = input("Category: ").lower()
        amount = int(input("Amount: "))

        expenses_log[category] = amount
        print("\n Expenses logged successfully")

    def friends_activities():

        activities = [a.strip().lower() for a in input("Friends: ").split(",")]
        activitiesByfriends = input("Friend's activities: ").split(",")

        activities_set =set(activities) 
        activitiesByfriends_set = set(activitiesByfriends)

        my_activities = activities_set.union(activitiesByfriends_set)
        print(f"All activities: {my_activities}" )

        mutual_activities =  activities_set.intersection(activitiesByfriends_set)
        print(f"mutual_activities: {mutual_activities}" )

        unique = activities_set.difference(activitiesByfriends_set)
        print(f"Unique: {unique}")

    def all_logs():
        print("\n---All Logs---")
        for task_name, (priority, time_bound) in smart_life.items():
            print(f"{task_name} -> Priority: {priority}, Time-bound: {time_bound}")


        for mood, time_of_day in mood_log.items():
            print(mood_log)

        for subject, hours in study_log.items():
            print(study_log)

        for category, amount in expenses_log.items():
            print(expenses_log)

    def search_input():
        search = input("What to search: ").lower()
        search_key = input("Search Key: ").lower()

        result = mood_log.get(search_key)
        if result:
            print(f"Your mood at {search} was: {result}")
        else:
            print("Time not found in log.")



    match choice:
        case 1:
            new_task()

        case 2:
            mood_entry()

        case 3:
            study_sessions()

        case 4:
            expenses()

        case 5:
            friends_activities()
        
        case 6:
            all_logs()

        case 7:
            search_input()

        case 8:
            print("Exiting Smart Life Assistant... Keep being awesome! 🚀")
            break
        
        case _:
            print("Oops! Invalid choice, try again")
