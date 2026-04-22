from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, periodicity):
        if periodicity not in ['daily', 'weekly']:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")

        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completion_dates = []

    def mark_as_completed(self):
        self.completion_dates.append(datetime.now())

    def get_current_streak(self):
        if not self.completion_dates:
            return 0

        sorted_dates = sorted(self.completion_dates)
        streak = 1
        
        for i in range(len(sorted_dates) - 1, 0, -1):
            diff = (sorted_dates[i] - sorted_dates[i - 1]).days

            if self.periodicity == 'daily' and diff <= 1:
                streak += 1
            elif self.periodicity == 'weekly' and diff <= 7:
                streak += 1
            else:
                break
        return streak

    def get_longest_streak(self):
        if not self.completion_dates:
            return 0

        sorted_dates = sorted(self.completion_dates)
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(sorted_dates)):
            diff = (sorted_dates[i] - sorted_dates[i - 1]).days

            if self.periodicity == 'daily' and diff <= 1:
                current_streak += 1
            elif self.periodicity == 'weekly' and diff <= 7:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)

    def to_dict(self):
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'created_at': self.created_at.isoformat(),
            'completion_dates': [c.isoformat() for c in self.completion_dates]
        }

    @staticmethod
    def from_dict(data):
        habit = Habit(data['name'], data['periodicity'])
        habit.created_at = datetime.fromisoformat(data['created_at'])
        habit.completion_dates = [datetime.fromisoformat(c) for c in data['completion_dates']]
        return habit