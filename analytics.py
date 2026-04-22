def get_all_habits(habits):
    return list(map(lambda h: h.name, habits))

def get_habits_by_periodicity(habits, periodicity):
    return list(filter(lambda h: h.periodicity == periodicity, habits))

def get_longest_streak_for_habit(habit):
    return habit.get_longest_streak()

def get_longest_streak_for_all_habits(habits):
    if not habits:
        return 0
    return max(map(lambda h: h.get_longest_streak(), habits))