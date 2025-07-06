class HabitTracker:
    def __init__(self, habit_name, status):
        self.habit_name = habit_name
        self.status = status

    def progress(self):
        if self.status == "done":
            return "Well done"
        
        elif self.status == "not yet":
            return "Keep pushing"
        
        else:
            return "Oops!"
        
habit1 = HabitTracker("Reading", "done")

print(habit1.progress())

        