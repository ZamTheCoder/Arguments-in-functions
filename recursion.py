num = int(input("Enter a positive number: "))

def factorial(num):
    if num == 1:
        return 1
    
    return  num * factorial(num - 1)

print(factorial(num))
