# calculator.py
# Interactive Python calculator using functions

# Function to get user input
def get_number(prompt):
    num = float(input(prompt))
    return num

# Function to perform calculations
def calculate(num):
    added = num + 10            # Step 1: add 10
    multiplied = added * 3      # Step 2: multiply by 3
    as_integer = int(multiplied) # Step 3: convert to integer
    return multiplied, as_integer

# Function to print results
def show_results(multiplied, as_integer):
    print("Result after multiplying:", multiplied)
    print("Final integer value:", as_integer)

# Main function to run the program
def main():
    num = get_number("Enter a number: ")
    multiplied, as_integer = calculate(num)
    show_results(multiplied, as_integer)

# Run the program
main()
