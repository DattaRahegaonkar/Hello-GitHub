#hello

# This code calculates the sum of all values in a dictionary


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

factorial_result = factorial(5)
# print(factorial_result)


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# print(prime(7))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    fnm1 = fibonacci(n - 1)
    fnm2 = fibonacci(n - 2)

    return fnm1 + fnm2

# print(fibonacci(4))


list = [1,2,3,2,1]

length = (int(len(list)))/2

for i in range(length):
    j=i+1
    if list[i] != list[-j]:
        print("Not a palindrome")
        break

# print(list)

