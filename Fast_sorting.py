def fast_sorting(arr):
    if len(arr)<2:
        return arr
    else:
        ind = len(arr)//2
        pivot_point = arr[ind]
        arr = arr[:ind]+arr[ind+1:]
        
        lower_then_pivot = [i for i in arr if i < pivot_point]
        higher_then_pivot = [i for i in arr if i >= pivot_point]
        print(lower_then_pivot)
        print(higher_then_pivot)
        return fast_sorting(lower_then_pivot) + [pivot_point] + fast_sorting(higher_then_pivot)
    
arr = fast_sorting([3,7,1,3,10,2,8,4])
print(arr)