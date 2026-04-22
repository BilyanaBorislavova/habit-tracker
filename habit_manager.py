from habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []

    def create_habit(self, habit, periodicity):
        habit = Habit(habit, periodicity)
        self.habits.append(habit)

    def delete_habit(self, name):
        habit = self.get_habit(name)
        if habit is None:
            return False
        self.habits.remove(habit)
        return True

    def get_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def get_habits(self):
        return self.habits

    def load_habits(self, habits):
        self.habits = habits

    