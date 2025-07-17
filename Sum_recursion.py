arr = [1,10,3,4,5]

def sum_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else: 
        return arr.pop(-1)+sum_recursion(arr)
    
sum = sum_recursion(arr)

print(sum)