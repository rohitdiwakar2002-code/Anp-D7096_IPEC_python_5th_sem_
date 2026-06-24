# Program to calculate remaining distribution

# Input: Total Pizza distribution and Number of Children
total_slices = int(input("Enter the total number of pizza distribution: "))
children = int(input("Enter the number of children: "))

# Calculation: Remaining slices after equal distribution
remaining_slices = total_slices % children   # Modulus gives the remainder

# Output: Display the remaining slices
print("Remaining Pizza Slices:", remaining_slices)
