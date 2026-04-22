from habit import Habit
from datetime import datetime, timedelta

def test_mark_as_completed():
    habit = Habit("Test Habit", "daily")
    habit.mark_as_completed()

    assert len(habit.completion_dates) == 1

def test_current_streak_daily():
    habit = Habit("Test Habit", "daily")

    now = datetime.now()
    habit.completion_dates = [
        now - timedelta(days=2),
        now - timedelta(days=1),
        now
    ]

    assert habit.get_current_streak() == 3

def test_current_streak_break():
    habit = Habit("Test Habit", "daily")

    now = datetime.now()
    habit.completion_dates = [
        now - timedelta(days=5),
        now
    ]

    assert habit.get_current_streak() == 1

def test_longest_streak_daily():
    habit = Habit("Test Habit", "daily")

    now = datetime.now()
    habit.completion_dates = [
        now - timedelta(days=5),
        now - timedelta(days=4),
        now - timedelta(days=1),
        now
    ]

    assert habit.get_longest_streak() == 2

def test_longest_streak_weekly():
    habit = Habit("Test Habit", "weekly")

    now = datetime.now()
    habit.completion_dates = [
        now - timedelta(weeks=3),
        now - timedelta(weeks=2),
        now - timedelta(weeks=1),
        now
    ]

    assert habit.get_longest_streak() == 4

def test_to_dict_and_from_dict():
    habit = Habit("Test Habit", "daily")
    habit.mark_as_completed()

    habit_dict = habit.to_dict()
    new_habit = Habit.from_dict(habit_dict)

    assert new_habit.name == habit.name
    assert new_habit.periodicity == habit.periodicity
    assert len(new_habit.completion_dates) == 1