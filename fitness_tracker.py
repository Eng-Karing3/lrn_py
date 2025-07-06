class Workout:

    def __init__(self, exercise, duration, intensity):
        self.exercise = exercise
        self.duration = int(duration)
        self.intensity = intensity

    def summary(self):
        if self.intensity == "high":
            return "Beast mode activated"
        
        elif self.intensity == "medium":
            return "Great effort, keep it up!"
        
        elif self.intensity == "low":
            return "Every step counts!"
        
        else:
            return "Oops!"
        
plan1 = Workout("Jogging", 30 , "medium")

print(plan1.summary())