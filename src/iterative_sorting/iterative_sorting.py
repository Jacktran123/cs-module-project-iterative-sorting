# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index=j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr)-1):
            current_index=i
            next_index=i + 1
            if arr[current_index] > arr[next_index]:
                arr[current_index],arr[next_index]=arr[next_index], arr[current_index]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if len(arr) > 0:
        max_element=max(arr)
        counting_arr=[0 for i in range(0,max_element + 2)]
        for i in range(0,len(arr)):
            for j in range(0,len(counting_arr)):
                if arr[i] == j:
                    counting_arr[j]+=1
                if arr[i]<0:
                    return ("Error, negative numbers not allowed in Count Sort")
        result_arr=[0 for i in range(len(arr))]
        for i in range(1,len(counting_arr)):
            counting_arr[i]+=counting_arr[i-1]
        for i in range(0,len(arr)):
            order=counting_arr[arr[i]]
            result_arr[order-1]=arr[i]
            counting_arr[arr[i]]-=1
        return result_arr
    else:
        return []

counting_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
