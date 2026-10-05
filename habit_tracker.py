habits = [
    ("Exercise", True),
    ("Read", False),
    ("Drink Water", True),
    ("Study Python", False)
]

for habit, completed in habits:
    if completed:
        print(habit, "- Completed")
    else:
        print(habit, "- Not completed")
        