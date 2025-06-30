import utils

name = input("Enter your name: ")
print(utils.greet_user(name))

hours = int(input("Enter number of hours: "))
print(utils.convert_into_minutes(hours))