from habit_manager import HabitManager

def test_create_and_get_habit():
    manager = HabitManager()
    manager.create_habit("Test Habit", "daily")

    habit = manager.get_habit("Test Habit")

    assert habit.name == "Test Habit"
    assert habit.periodicity == "daily"

def test_delete_habit():
    manager = HabitManager()
    manager.create_habit("Test Habit", "daily")

    manager.delete_habit("Test Habit")

    result = manager.get_habit("Test Habit")
    assert result is None

def test_get_habits():
    manager = HabitManager()
    manager.create_habit("Test Habit 1", "daily")
    manager.create_habit("Test Habit 2", "weekly")

    habits = manager.get_habits()
    assert len(habits) == 2
    assert habits[0].name == "Test Habit 1"
    assert habits[1].name == "Test Habit 2"