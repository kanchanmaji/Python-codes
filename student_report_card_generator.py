# 📘 Student Report Card Generator

def average(marks):
    """Return average of marks"""
    return sum(marks.values()) / len(marks)

def grade(avg):
    """Return grade based on average"""
    if 90 <= avg <= 100:
        return "A"
    elif 75 <= avg < 90:
        return "B"
    elif 60 <= avg < 75:
        return "C"
    else:
        return "D"

print("\n |--- Enter Your Details Below ---|")
name = input("\n## Enter Your Name ☆\n---> ")

# Dictionary to store subject marks
subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]
marks = {}

for sub in subjects:
    marks[sub] = float(input(f"\n☆ Enter {sub} marks /100 ☆\n---> "))

# Calculate average & grade
avg = average(marks)
student_grade = grade(avg)

# Find subject with highest marks (using lambda + max)
top_subject = max(marks, key=lambda x: marks[x])

# 🖨️ Print Report Card
print("\n" + "="*35)
print("         📄 STUDENT REPORT CARD")
print("="*35)
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Average: {avg:.2f}")
print(f"Highest Scored Subject: {top_subject} ({marks[top_subject]})")
print(f"Grade: {student_grade}")
print("="*35)