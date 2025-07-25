"""This module contains basic examples of recursion and palindrome checking."""

def factorial(n):
    """Return the factorial of a number."""
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


factorial_result = factorial(5)
# print(factorial_result)


def prime(n):
    """Check if a number is prime."""
    for idx in range(2, n):
        if n % idx == 0:
            return False
    return True

# print(prime(7))


def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n in (0, 1):
        return n

    fnm1 = fibonacci(n - 1)
    fnm2 = fibonacci(n - 2)

    return fnm1 + fnm2

# print(fibonacci(4))


input_list = [1, 2, 3, 2, 1]
half_length = int(len(input_list) / 2)

for idx in range(half_length):
    if input_list[idx] != input_list[-(idx + 1)]:
        print("Not a palindrome")
        break

# print(input_list)

