# Program to calculate Class room Seating arrangement

# Input: Total Students and Students seat in room
total_students = int(input("Enter the total number of seat: "))
students_per_row = int(input("Enter the number of students per seat: "))

# Calculation:
complete_rows = total_students // students_per_row   # Integer division

# Output: Display the number of room seat arrangement
print("Number of Complete Rows:", complete_rows)
