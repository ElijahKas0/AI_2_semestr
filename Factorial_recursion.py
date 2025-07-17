def factorial_calculation(x):
    print(x-1)
    if x == 1:
        return 1
    else:
        return x*factorial_calculation(x-1)
        

res = factorial_calculation(5)
print(res)