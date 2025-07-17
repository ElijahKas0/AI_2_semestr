arr = [1,2,3,4,5]

def binary_search(arr,item):
    low_boundary = 0
    high_boundary = len(arr)-1

    while low_boundary<=high_boundary:
        print(low_boundary,high_boundary)
        middle_item_index = (low_boundary+high_boundary)//2
        if arr[middle_item_index] == item:
            return middle_item_index
        elif arr[middle_item_index]>item:
            high_boundary = middle_item_index-1
        elif arr[middle_item_index]<item:
            low_boundary = middle_item_index+1
        else:
            return None
        
ind = binary_search(arr,4)
print(ind)
ind = binary_search(arr,90)
print(ind)