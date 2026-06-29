''' Write a program to calculate area and perimeter of rectangle and validate it'''
# Step 1: Define a function to calculate area and perimeter of a rectangle

def calculate_rectangle(length, width):

    # Step 2: Validate inputs
    # Length and width must be positive numbers, otherwise return an error message
    if length <= 0 or width <= 0:
        return "Error: Length and width must be positive numbers."
    
    # Step 3: Calculate area using formula: Area = length * width
    area = length * width
    
    # Step 4: Calculate perimeter using formula: Perimeter = 2 * (length + width)
    perimeter = 2 * (length + width)
    
    # Step 5: Return the results in a formatted string
    return f"Area: {area}, Perimeter: {perimeter}"

# Step 6: Main program starts here
try:
    # Step 7: Take user input for length and width
    # Convert input values to float to allow decimal values
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Step 8: Call the function and store the result
    result = calculate_rectangle(length, width)

    #-----------------------------------#
    ''' Output of the rectangle '''
    # Step 9: Print the result (either area & perimeter or error message)
    print(result)

# Step 10: Handle invalid input (like entering text instead of numbers)
except ValueError:
    print("Error: Please enter valid numeric values.")
