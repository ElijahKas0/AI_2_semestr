def searching_smallest(arr):
    smallest_ind = 0

    for i in range(len(arr)):
        if arr[i]<arr[smallest_ind]:
            smallest_ind = i
    return smallest_ind

def sorting_by_choosing(arr):
    new_arr = []
    while arr != []:
        print(arr)
        current_smallest_ind = searching_smallest(arr)
        new_arr.append(arr.pop(current_smallest_ind))
    else:
        print(new_arr)

sorting_by_choosing([4,24,1,3,2,15,16,78,22,13])

