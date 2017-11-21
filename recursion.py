
def factorial(n):
    if n == 1:
        # print(n)
        return 1
    else:
        answer = n * factorial(n-1)
        # print("The answer is",answer)
        return answer

print("factorial of 10:", factorial(10))


def gcd(a,b):
    '''find and return the greatest common devisor
    of two inputs, using recursion.'''
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(1022,2011))

def is_palindrome(word):
    if (len(word) == 1) or (len(word) == 0):
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

print(is_palindrome("hannah"))
print(is_palindrome("laurel"))

def fibonacci(n):
    pass
