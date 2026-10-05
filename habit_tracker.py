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


def habit_report(habits):
    completed = sum(1 for habit, status in habits if status)
    total = len(habits)

    print("\nHabit Report")
    print("Completed:", completed)
    print("Total habits:", total)
    print("Completion rate:", (completed / total) * 100, "%")


habit_report(habits)