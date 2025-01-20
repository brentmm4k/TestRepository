# Example of a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}
print(student)

# Using curly braces
student_info = {
    "name": "Bob",
    "age": 21,
    "major": "Computer Science"
}

# Using dict function
student_info2 = dict(name="Emma", age=22, major="Biology")

print(student_info)
print(student_info2)

student = {
    "name": "Charlie",
    "age": 19,
    "major": "Physics"
}

# Accessing using key
print(student["name"])   # Output: Charlie

# Using .get() to access key safely
print(student.get("GPA", "Not Available"))  # Output: Not Available