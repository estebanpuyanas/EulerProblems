"""
Problem 4: Largest Palindromic Product of 2 three-digit numbers.
Objective: Find the largest product of 2 three-digit numbers that is palindormic. 
A palindrome is a number that reads the same forward and backwords. 
"""

import math

def largest_palindrome_same_size(num_length):

    max_palindromic = 0

    high = int(math.pow(10, num_length) - 1)
    low = int(math.pow(10, num_length - 1))         
    
    for i in range(high, low - 1, -1):
        for j in range(i, low - 1, -1):
            product = i * j
            if product <= max_palindromic:
                break
            if is_palindrome(product) and product > max_palindromic:
                max_palindromic = product
    
    return max_palindromic
             
def is_palindrome(number):

    num_string = str(number)
    length = len(num_string)

    for index in range(length // 2):
        if num_string[index] != num_string[length - index - 1]:
            return False
    return True

def main():

    length = 3
    result = largest_palindrome_same_size(length)
    print(result)

main()