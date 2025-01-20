# Function to get student data
def get_student_data():
    student_grades = {}
    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {name}: "))
            student_grades[name] = grade
        except ValueError:
            print("Invalid grade. Please enter a number.")
    return student_grades

# Function to calculate statistics
def calculate_statistics(student_grades):
    if not student_grades:
        return None
    
    average_grade = sum(student_grades.values()) / len(student_grades)
    highest_student = max(student_grades, key=student_grades.get)
    lowest_student = min(student_grades, key=student_grades.get)
    return {
        'average': average_grade,
        'highest': (highest_student, student_grades[highest_student]),
        'lowest': (lowest_student, student_grades[lowest_student])
    }

# Function to display results
def display_results(student_grades, statistics):
    if not student_grades:
        print("No student data to display.")
        return
    
    print("\n--- Student Grades ---")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")
    
    print("\n--- Statistics ---")
    print(f"Average Grade: {statistics['average']:.2f}")
    print(f"Highest Grade: {statistics['highest'][0]} ({statistics['highest'][1]})")
    print(f"Lowest Grade: {statistics['lowest'][0]} ({statistics['lowest'][1]})")

# Main Program
if __name__ == "__main__":
    student_grades = get_student_data()
    statistics = calculate_statistics(student_grades)
    display_results(student_grades, statistics)