'''
Created on 03-Jul-2024

@author: subhashis
'''

def factorial_iterative(n):
    """Calculate the factorial of a number using an iterative approach."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate the factorial of a number using a recursive approach."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"Iterative approach: Factorial of {number} is {factorial_iterative(number)}")
    print(f"Recursive approach: Factorial of {number} is {factorial_recursive(number)}")

if __name__ == "__main__":
    main()

