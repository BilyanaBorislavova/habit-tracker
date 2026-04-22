import json
from habit import Habit

def save_habits(habits, filename="habits.json"):
    with open(filename, 'w') as f:
        json.dump([h.to_dict() for h in habits], f)

def load_habits(filename="habits.json"):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if not content:
                return []
            habits_data = json.loads(content)
            return [Habit.from_dict(h) for h in habits_data]
    except FileNotFoundError:
        return []
