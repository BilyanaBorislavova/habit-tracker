from habit import Habit
from datetime import datetime, timedelta

def create_predefined_habits():
    number_of_days_in_four_weeks = 28
    number_of_weeks_in_four_weeks = 4

    predefined_habits = [
        Habit("Drink water", "daily"),
        Habit("Exercise", "daily"),
        Habit("Read a book", "daily"),
        Habit("Meditate", "weekly"),
        Habit("Clean the house", "weekly"),
    ]

    now = datetime.now()

    for habit in predefined_habits:
        if habit.periodicity == "daily":
            for i in range(number_of_days_in_four_weeks):
                habit.completion_dates.append(now - timedelta(days=i))
        elif habit.periodicity == "weekly":
            for i in range(number_of_weeks_in_four_weeks):
                habit.completion_dates.append(now - timedelta(weeks=i))
    return predefined_habits