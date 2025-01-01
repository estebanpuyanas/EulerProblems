"""
Problem 5: 10001 Prime Number
Objective: Find the 10001th prime number. 
"""
import math

def nth_prime_number(target):
    return None

def is_prime(number):

    if number == 0:
        return False
    if number == 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
    
    
    





    
def main():

    number = 10001
    result = largest_prime(number)
    print(result)

    main()