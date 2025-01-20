student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}

print("Name:", student["Name"])
print("Major:", student["Major"])


student["GPA"] = 3.8
student["Age"] = 25

print(student)

for key, value in student.items():
    print(f"{key}: {value}")


def check_key(dictionary, key):
    if key in dictionary:
        return "Key exists"
    else:
        return "Key does not exist"

# Testing the function
print(check_key(student, "Name"))  # Output: Key exists
print(check_key(student, "Hobbies"))  # Output: Key does not exist

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)