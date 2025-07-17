arr = [1,2,3,4,5,6,7,8,9,10]

def counting_recursion(arr):
    if len(arr) == 1:
        return 1
    else:
        arr.pop(-1)
        print(arr)
        return 1 + counting_recursion(arr)
    
result = counting_recursion(arr)

print(result)