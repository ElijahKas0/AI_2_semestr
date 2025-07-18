arr = [100000, 30, 1000, 1, 800]

def largest_recursion(arr,x,digit):
    if len(arr) == 1:
        return x, digit
    else:
        if arr[-1]>digit:
            x = len(arr)-1
            digit = arr[x]
        arr.pop(-1)
        return largest_recursion(arr,x,digit)

ind, digit = largest_recursion(arr,0,arr[0])

print(ind,digit)