import datetime

class WorkoutTracker:
    def __init__(self, name, sex, age, weight, height, weight_unit='kg', height_unit='cm'):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.height = height
        self.weight_unit = weight_unit
        self.height_unit = height_unit
        self.workout_data = []
        self.bmi = self.calculate_bmi()

    def calculate_bmi(self):
        if self.height_unit == 'cm':
            height_in_m = self.height / 100
        elif self.height_unit == 'in':
            height_in_m = self.height * 0.0254
        else:
            raise ValueError("Invalid height unit")

        if self.weight_unit == 'kg':
            weight_in_kg = self.weight
        elif self.weight_unit == 'lb':
            weight_in_kg = self.weight * 0.453592
        else:
            raise ValueError("Invalid weight unit")

        bmi = weight_in_kg / (height_in_m ** 2)
        return bmi

    def add_workout(self, day, steps, time_str):
        time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
        time_in_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        distance = steps * 0.000762  # Assuming an average step length of 0.76 meters
        speed = distance / (time_in_seconds / 3600)
        self.workout_data.append((day, distance, speed))

    def generate_report(self):
        num_workouts = len(self.workout_data)
        if num_workouts == 0:
            return "No workout data available."

        total_distance = sum(workout[1] for workout in self.workout_data)
        total_speed = sum(workout[2] for workout in self.workout_data)
        average_speed = total_speed / num_workouts
        average_distance = total_distance / num_workouts

        min_speed = min(workout[2] for workout in self.workout_data)
        max_speed = max(workout[2] for workout in self.workout_data)
        min_distance = min(workout[1] for workout in self.workout_data)
        max_distance = max(workout[1] for workout in self.workout_data)

        report = f"Hi {self.name},\n"
        report += f"Your BMI is: {self.bmi:.1f}\n"
        report += f"Your Weekly achievement is as follows:\n"
        report += f"No breakout in Sessions: You get a {num_workouts}/7 award\n"
        report += f"Your Fastest Speed is: {max_speed:.2f} Km/hr\n"
        report += f"Your Longest Distance is: {max_distance:.1f} km\n"
        report += f"Your Slowest Speed is: {min_speed:.2f} Km/hr\n"
        report += f"Your Shortest Distance is: {min_distance:.1f} Km\n"
        report += f"Your Weekly Average Speed is: {average_speed:.2f} Km/hr\n"
        report += f"Your Weekly Average Distance is: {total_distance:.2f} Km\n"

        return report

if __name__ == '__main__':
    print("Welcome to the Workout Tracker App!")
    print("------------------------------------")
    
    name = input("Name: ")
    sex = input("Sex (Male/Female): ")
    age = int(input("Age (years): "))
    weight = float(input("Weight (in Kg or Lbs): "))
    weight_unit = input("Weight unit (kg/lb): ")
    height = float(input("Height (in cm or inches): "))
    height_unit = input("Height unit (cm/in): ")

    workout_tracker = WorkoutTracker(name, sex, age, weight, height, weight_unit, height_unit)

    num_workouts = int(input("Enter the number of workout sessions to input: "))

    for i in range(num_workouts):
        print(f"Workout {i+1}:")
        day = int(input("Day (1 for Monday, 2 for Tuesday, etc.): "))
        steps = int(input("Number of steps: "))
        time_str = input("Time taken (hours:minutes:seconds): ")
        workout_tracker.add_workout(day, steps, time_str)

    print(workout_tracker.generate_report())
