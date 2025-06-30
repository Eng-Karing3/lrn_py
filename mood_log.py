mood_log = {}

def add_mood():
    mood = input("Enter your current mood: ")
    time_of_day = input("Enter time of the day: ")

    mood_log[mood] = time_of_day

    motivate = lambda mood:(
        "Don't kill the vibe" if mood== "happy"
        else "cheer up mate" if mood == "sad"
        else "Relax mate" if mood == "stressed"
        else "take care"
    )

    print(f"Mood logged! {motivate(mood)}")

def view_log():
    for mood, time_of_day in mood_log.items():
        print(f"{mood} -> {time_of_day}")



def search_time():
    search = input("Enter period of time: ")

    result = mood_log.get(search)
    if result:
        print(f"Your mood at {search} was: {result}")
    else:
        print("Time not found in log.")



while True:
    print("1. Add Mood")
    print("2. View All Logs")
    print("3. Search by Time")
    print("4. Exit")

    choice = input("What's your option: ")

    if choice == "1":
       add_mood()

    elif choice == "2":
        view_log()

    elif choice == "3":
        search_time()

    elif choice == "4":
        print("Exiting, Enjoy your day")
        break
    else:
        print("Oops! Invalid choice try again")