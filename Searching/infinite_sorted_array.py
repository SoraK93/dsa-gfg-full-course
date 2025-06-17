'''This module is used to solve problem related to infinite sized array'''
infinite_array = [1, 10, 15, 20, 40, 80, 90, 100, 120, 500]
X = 100

# given array we have to find position of the lookup_value in the array
# Require a array to look into
# Require a value to search for
# Since its a sorted array, we can apply binary array
# array[n] represents center
# if value is less than current array[n0] go to left side
# if value is more than current array[0n] go to right side
# if value is equal just return the position
# How are we tracking position?

# Binary Solution
def inf_array_binary_func(arr, lookup_value):
    """Used for sorting arrays based on binary sort algorithm"""
    not_found = True
    array_length = len(arr)
    start, end= 0, array_length

    while not_found:
        mid = (start + end) // 2

        if arr[mid] == lookup_value:
            return mid
        if arr[mid] < lookup_value:
            start = mid + 1
            mid = (start + end) // 2
        elif arr[mid] > lookup_value:
            end = mid
            mid = (start + end) // 2

        if start >= end:
            not_found = False
            return -1

        # print(start, end, mid)

# Binary Solution - Alt
def inf_array_altbinary_func(arr, lookup_value):
    '''This is using a alternate binary search algorithm'''
    if arr[0] == lookup_value:
        return 0
    i = 1
    while arr[i] < lookup_value:
        i = i * 2
    if arr[i] == lookup_value:
        return i
    return bsearch(arr, i // 2 + 1, i - 1, lookup_value)

def bsearch(arr, start, end, lookup_value):
    '''This function checks the range between start and end params 
    searching for lookup_value in the array'''
    for i in range(start, end + 1):
        if arr[i] == lookup_value:
            return i
    return -1

# Loop Solution
def inf_array_loop_func(arr, lookup_value):
    '''Using loop while trying to find index of the given value inside a infinite array'''
    index = 0
    not_found = True
    while not_found:
        if arr[index] == lookup_value:
            not_found = False
            return index
        if arr[index] > lookup_value:
            return -1
        index += 1


BINARY_RESULT = inf_array_binary_func(infinite_array, X)
ALT_BINARY_RESULT = inf_array_altbinary_func(infinite_array, X)
LOOP_RESULT = inf_array_loop_func(infinite_array, X)

print("Position based on binary search:", BINARY_RESULT)
print("Position based on alt binary search:", ALT_BINARY_RESULT)
print("Position based on Loop search:", LOOP_RESULT)
