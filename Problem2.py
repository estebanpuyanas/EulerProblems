"""
Problem 2: Even Fibonacci Numbers
Objective: Find the sum of all even Fibonacci numbers below 4000000
"""

def even_fib_sum(limit):

    num1, num2  = 1, 2

    even_sum = 0 

    while num1 <= limit:
        if num1 % 2 == 0:
            even_sum += num1

    num1 = num2
    num2 = num1 + num2

    return even_sum
   


def main():

    limit = 4000000

    result = even_fib_sum(limit)
    
    print(result)

main()


        
        

    




    