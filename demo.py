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
    for i in range(2, n):  # renamed from 'idx' to 'i'
        if n % i == 0:
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
half_len = int(len(input_list) / 2)  # renamed to avoid constant naming warning

for index in range(half_len):  # renamed from 'idx' to 'index'
    if input_list[index] != input_list[-(index + 1)]:
        print("Not a palindrome")
        break

# print(input_list)

