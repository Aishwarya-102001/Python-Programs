def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(factorial_iter(7))

#********************************

def sum(n):
    for i in range(n):
        sum = sum(n-1) + n
    return sum

print(sum(3))