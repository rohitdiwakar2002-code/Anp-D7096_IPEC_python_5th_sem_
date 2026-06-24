# Program to calculate Compound Growth of Savings

# Input: Initial Amount and Number of Years
initial_amount = float(input("Enter the initial investment amount: "))
years = int(input("Enter the number of years: "))

# Calculation: Final Amount (doubles every year)
final_amount = initial_amount * (2 ** years)

# Output: Display the final amount
print("Final Amount after", years, "years: ₹", final_amount)
