def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

factorial_result = factorial(5)
print(factorial_result)
