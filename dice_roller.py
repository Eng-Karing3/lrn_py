import random

def roll_dice():
    return random.randint(1, 6)

print(f"You rolled: {roll_dice()}")