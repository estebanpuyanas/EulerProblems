"""
Problem 5: Sum square difference. 
Objective: The sum of the squares of n numbers is defined as: 
n0^2 + n1^2 + n2^2 + ... + nn^2. For example, for the first ten numbers (1-10), 
the sum of the squares can be seen as: 1^2 + 2^2 + 3^ + ... 10^2 = 385. 

On the other hand, the square of the sum of n numbers can be defined as:
(n0 + n1 +n2 + ... + nn)^2. For example for the first ten numbers (1-10), this can be seen as: 
(1 + 2 + 3 + ... + 10)^2
"""

import math

def sum_square_diff(start, end):
    return square_of_sum(start, end) - sum_of_squares(start, end)

def sum_of_squares(start, end):

    number_list = [i for i in range(start, end + 1)]

    for i in range(len(number_list)):
        number_list[i] = int(math.pow(number_list[i],2))

    return sum(number_list)

def square_of_sum(start, end):

    number_list = [i for i in range(start, end + 1)]
    number_list = sum(number_list)
    number_list = int(math.pow(number_list, 2))

    return number_list

def main():
    
    start = 1
    end = 100

    result = sum_square_diff(start, end)

    print(result)

main()