"""
Problem 3: Largest Prime Factor
Objective: Find the largest prime factor of 600851475143
"""

import math


def largest_prime(target):
    i = 2

    while i * i <= target:
        while target % i == 0:
            target = target / i
        i = i + 1

    return target


def main():
    target = 600851475143
    result = largest_prime(target)
    print(result)


main()
