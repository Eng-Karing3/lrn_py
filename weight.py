class HealthProfile:

    def __init__(self):
        self.__weight = "Private"

    def get_weight(self):
        return self.__weight
    
    def add_weight(self, new_weight):
        self.__weight = new_weight

w = HealthProfile()

print(w.get_weight())

w.add_weight("10kg")
print(w.get_weight())
        

    

