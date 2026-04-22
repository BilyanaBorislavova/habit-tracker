from habit_manager import HabitManager
from predefined_habits import create_predefined_habits
from habit import Habit
from analytics import (
    get_habits_by_periodicity,
    get_longest_streak_for_habit,
    get_longest_streak_for_all_habits
)
from storage import save_habits, load_habits


def main():
    manager = HabitManager()
    habits = load_habits()

    if not habits:
        habits = create_predefined_habits()

    manager.load_habits(habits)

    while True:
        print("\n1. Create a new habit")
        print("2. Delete a habit")
        print("3. Mark habit as completed")
        print("4. View all habits")
        print("5. View habits by periodicity")
        print("6. View longest streak for a habit")
        print("7. View longest streak for all habits")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter habit name: ").strip()
            periodicity = input("Enter periodicity (daily/weekly): ").strip()

            if periodicity not in ['daily', 'weekly']:
                print("Invalid periodicity. Use 'daily' or 'weekly'.")
                continue

            manager.create_habit(name, periodicity)
            save_habits(manager.get_habits())
            print("Habit created successfully.")

        elif choice == '2':
            name = input("Enter habit name to delete: ").strip()

            before = len(manager.get_habits())
            manager.delete_habit(name)
            after = len(manager.get_habits())

            if before == after:
                print(f"Habit not found: {name}")
            else:
                save_habits(manager.get_habits())
                print("Habit deleted successfully.")

        elif choice == '3':
            name = input("Enter habit name to mark as completed: ").strip()
            habit = manager.get_habit(name)

            if isinstance(habit, Habit):
                habit.mark_as_completed()
                save_habits(manager.get_habits())
                print("Habit marked as completed.")
            else:
                print(habit)

        elif choice == '4':
            for habit in manager.get_habits():
                if habit.completion_dates:
                    completed_dates = ", ".join(d.strftime('%Y-%m-%d') for d in habit.completion_dates)
                else:
                    completed_dates = "No completions yet"

                print(f"{habit.name} ({habit.periodicity}) - Completed on: {completed_dates}")

        elif choice == '5':
            periodicity = input("Enter periodicity (daily/weekly): ").strip()

            filtered = get_habits_by_periodicity(manager.get_habits(), periodicity)

            for habit in filtered:
                completed_dates = ", ".join(d.strftime('%Y-%m-%d') for d in habit.completion_dates)
                print(f"{habit.name} ({habit.periodicity}) - Completed on: {completed_dates}")

        elif choice == '6':
            name = input("Enter habit name: ").strip()
            habit = manager.get_habit(name)

            if isinstance(habit, Habit):
                streak = get_longest_streak_for_habit(habit)
                print(f"Longest streak for {habit.name}: {streak}")
            else:
                print(habit)

        elif choice == '7':
            streak = get_longest_streak_for_all_habits(manager.get_habits())
            print(f"Longest streak across all habits: {streak}")

        elif choice == '8':
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()