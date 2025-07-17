arr = [10, 30, 150, 1, 800]

def largest_recursion(arr,x,digit):
    if len(arr) == 1:
        return x
    else: 
        print(arr[-1],'xxx')
        if arr[-1]>digit:
            x = len(arr)-1
            # print(x)
        digit = arr[x]
        arr.pop(-1)
        print(x)
        return largest_recursion(arr,x,digit)

result = largest_recursion(arr,0,arr[0])

print(result)