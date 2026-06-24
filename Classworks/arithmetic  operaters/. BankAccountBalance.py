# Program to calculate bank Account balance

# Input: Current Balance and Withdrawal Amount
current_balance = float(input("Enter your current balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))

# Check if withdrawal is possible
if withdrawal_amount > current_balance:
    print("Insufficient balance! Withdrawal not possible.")
else:
    # Calculation: Remaining Balance
    remaining_balance = current_balance - withdrawal_amount
    # Output: Display the remaining balance
    print("Remaining Balance: ₹", remaining_balance)
