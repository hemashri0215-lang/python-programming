"""
01_variables.py
---------------
Demonstrates Python variables and basic data types.
"""

# Student information
name = "Hema"
age = 21
year_of_study = 3
course = "B.Tech IT"
university = "Pondicherry University"

# Academic information
gpa = 8.5
is_graduating_soon = False

# Calculate remaining study years
years_left = 4 - year_of_study

# Display student information
print("=" * 45)
print("           STUDENT PROFILE")
print("=" * 45)

print(f"Student Name       : {name}")
print(f"Age                : {age}")
print(f"Course             : {course}")
print(f"Year of Study      : {year_of_study}")
print(f"University         : {university}")
print(f"Current GPA        : {gpa}")
print(f"Graduating Soon?   : {is_graduating_soon}")
print(f"Years Left         : {years_left}")

print("=" * 45)