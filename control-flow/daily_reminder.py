task = input("Enter your task:")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(
                "Reminder",
                task,
                "is a high priority task that requires immediate attention today!",
            )
        else:
            print(
                "Note:",
                task,
                ", is a high priority task. Consider completing it when you have free time.",
            )
    case "medium":
        if time_bound == "yes":
            print(
                "Reminder:",
                task,
                "is a medium priority task that needs to be done today.",
            )
        else:
            print(
                "Note:",
                task,
                ", is a medium priority task. Consider completing it when you have free time.",
            )
    case "low":
        if time_bound == "yes":
            print(
                "Reminder:", task, "is a low priority task that needs to be done today."
            )
        else:
            print(
                "Note:",
                task,
                ", is a low priority task. Consider completing it when you have free time.",
            )
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
