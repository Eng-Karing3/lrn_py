mood = {}

while True:
    print("Add a mood")
    print("View all logs")
    print("view all moods")
    print("view all times")
    print("search mood at a specific time")
    print("Exit")

    select= input("Enter your choice: ")

    match select:
        case "1":
            current_mood = input("What are you feeling now: happy, sad stressed? ")
            time = input("What's the time of the day: morning evening midday? ")

            mood[current_mood] = time

            motivate = lambda mood: "Keep smiling! 😊" if mood == "happy" else "Hang in there 💪"
            print(motivate)

            motivate = lambda mood: "Worry less 😊" if mood == "sad" else " Keep smiling! 😊"
            print(motivate)

            motivate = lambda mood: "Relax mate 😊" if mood == "stressed" else "Keep smiling! 😊"
            print(motivate)

        case "2":
            print("\n---All logs---")

            for current_mood, time in mood.items():
                print(f"{current_mood} > {time}")

        case "3":
            for current_mood in mood.keys():
                print(f"{current_mood}")

        case "4":
            for time in mood.values():
                print(f"{time}")

        case "5":
            search = input("specific time: ").lower
            result = mood.get(search)

            if result:
                print(f"During {search} your mood was {result}")

            else:
                print("Oops! try again")

        case "6":
            print("Exiting, Ciao")
            break

        case _:
            print("Almost there, Input correct choice!")



      