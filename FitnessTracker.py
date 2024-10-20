import json
from datetime import datetime

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.load_data()

    def load_data(self):
        try:
            with open('workouts.json', 'r') as file:
                self.workouts = json.load(file)
        except FileNotFoundError:
            self.workouts = []

    def save_data(self):
        with open('workouts.json', 'w') as file:
            json.dump(self.workouts, file)

    def add_workout(self):
        date = input("Enter workout date (YYYY-MM-DD): ")
        activity = input("Enter activity type (e.g., Running, Cycling): ")
        duration = float(input("Enter duration in minutes: "))
        calories_burned = float(input("Enter calories burned: "))

        workout = {
            'date': date,
            'activity': activity,
            'duration': duration,
            'calories_burned': calories_burned
        }
        self.workouts.append(workout)
        self.save_data()
        print("Workout added successfully!")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts logged.")
            return

        print("\n--- Workout History ---")
        for workout in self.workouts:
            print(f"Date: {workout['date']}, Activity: {workout['activity']}, "
                  f"Duration: {workout['duration']} mins, Calories Burned: {workout['calories_burned']}")

    def calculate_total_calories(self):
        total_calories = sum(workout['calories_burned'] for workout in self.workouts)
        print(f"\nTotal Calories Burned: {total_calories}")

    def main_menu(self):
        while True:
            print("\n--- Fitness Tracker ---")
            print("1. Add Workout")
            print("2. View Workouts")
            print("3. Calculate Total Calories Burned")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_workout()
            elif choice == '2':
                self.view_workouts()
            elif choice == '3':
                self.calculate_total_calories()
            elif choice == '4':
                print("Exiting program. Thank you for using the Fitness Tracker!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    tracker = FitnessTracker()
    tracker.main_menu()
