def is_armstrong(num):
    # Count number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the number is Armstrong or not
    if sum_of_powers == num:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
