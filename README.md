# Habit Tracker App (Python)

## Overview
This project is a habit tracking application developed in Python. It allows users to create, delete, manage and analyze habits with daily or weekly periodicity by using the command line interface.

The app follows object oriented design for habit management and functional programming for analytics.

## Features
- Create and delete habits
- Track habit completion over time
- Support for daily and weekly habits
- View all habits and filter by periodicity
- Calculate:
    - Current streak
    - Longest streak for a habit
    - Longest streak across all habits
- Predefined habits with 4 weeks of sample data
- Persistent storage using JSON
- Command Line Interface
- Unit tests using pytest

## Installation
1. Clone the repository
git clone // add git path here
cd habit-tracker

2. Install dependencies
Make sure you have Python 3.7 or any version above installed.

Install pytest for testing.

## Running the Application
Start the CLI:

python main.py

You will see a menu with options to:
1. Create a new habit 
2. Delete habit
3. Mark habit as completed
4. View all habits
5. View habits by periodicity
6. View longest streak for a habit
7. View longest streak for all habits
8. Exit

## Running Tests
Run all tests by using pytest. Make sure you are in the correct directory when running them:
habit-tracker/tests

## Example Usage
From the main project directory (habit-tracker), run python main.py
All the options will display.
Choose 1 to create a new habit.
You will need to enter the following data:
Enter habit name: Exercise
Enter periodicity: daily
Then mark it as completed.
Then view streak analysis.

## Predefined Habits
The application includes 5 predefined habits with 4 weeks of tracking data:
- Daily habits ("Drink water", "Exercise", "Read a book")
- Weekly habits ("Meditate", "Clean the house")
These are automatically loaded if no saved data exists.

## Notes
- A habit streak is considered broken if a task is not completed within its defined period.
- Broken habits are handled through streak calculation logic.

## Author
Bilyana Borislavova

