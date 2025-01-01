"""
Problem 1: Multiples of 3 or 5
Objective: Find the sum of all the multiples below 3 or 5 below 1000
"""

def multipleCounter(limit):

    result_list = []

    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            result_list.append(i)
    
    sum_result = sum(result_list)

    return sum_result

def main():

    result = multipleCounter(1000)
    print(result)

main()