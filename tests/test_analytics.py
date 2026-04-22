from habit import Habit
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_for_habit,
    get_longest_streak_for_all_habits
)
from datetime import datetime, timedelta

def create_sample_habits():
    now = datetime.now()

    habit_one = Habit("Daily Exercise", "daily")
    habit_one.completion_dates = [
        now - timedelta(days=2),
        now - timedelta(days=1),
        now
    ]

    habit_two = Habit("Weekly Reading", "weekly")
    habit_two.completion_dates = [
        now - timedelta(weeks=2),
        now - timedelta(weeks=1),
        now
    ]

    return [habit_one, habit_two]

def test_get_all_habits():
    habits = create_sample_habits()
    habit_names = get_all_habits(habits)

    assert habit_names == ["Daily Exercise", "Weekly Reading"]

def test_get_habits_by_periodicity():
    habits = create_sample_habits()

    daily_habits = get_habits_by_periodicity(habits, "daily")
    weekly_habits = get_habits_by_periodicity(habits, "weekly")

    assert len(daily_habits) == 1
    assert len(weekly_habits) == 1

def test_longest_streak_for_habit():
    habits = create_sample_habits()

    result = get_longest_streak_for_habit(habits[0])
    assert result == 3

def test_longest_streak_for_all_habits():
    habits = create_sample_habits()

    result = get_longest_streak_for_all_habits(habits)
    assert result == 3
