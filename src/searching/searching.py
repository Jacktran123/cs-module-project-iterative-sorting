def linear_search(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr.sort()
    min_value=0
    max_value=(len(arr) - 1)
    while max_value >= min_value:
        middle=(min_value + max_value) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            max_value= middle - 1
        elif target > arr[middle]:
            min_value= middle + 1
    return -1
