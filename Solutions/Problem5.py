"""
Problem 5: Smallest evenly-divisible number by all the numbers between 1-20.
Objective: Find the samllest number that is evenly divisble by all the numbers between 1 and 20. 
A number is evenly divisible if there is no remainder. 
"""

def smallest_evenly_divisble(start, end):

    # Since the algo is generalized to find the LCM of a number from a,b set the result to start
    result = start

    # In loop, set it to go from start + 1 and end + 1 bc you do not need to do first iteration and include the last number.
    for num in range(start + 1, end + 1):

        # Use LCM formula where LCM(a, b) = abs(a * b) / GCD(a, b)
        # Given that result is set to start, think that result = a, and num (current index in loop) = b
        result = abs(result * num) // eucledian_gcd(result, num)
    
    return result

# Simple implementation of Eucledian algorithm for learning purposes. Can use math.gcd() for built-in functionality. 
def eucledian_gcd(num1, num2):

    # Convert input to absolute value to deal with negative
    num1 = abs(num1)
    num2 = abs(num2)

    # Base case: both numbers are = 0.
    if num1 == 0 and num2 == 0:
        return 0
    # Base case: either number is 0, return the other.
    elif num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    
    # Base case: GCD has been found.
    if num1 % num2 == 0:
        return num2
    
    return eucledian_gcd(num2, num1 % num2)

def main():

    start = 1
    end = 20

    result = smallest_evenly_divisble(start, end)
    print(result)

main()