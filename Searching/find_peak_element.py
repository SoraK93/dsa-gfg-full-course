'''Find a Peak Element'''
arr = [10, 20, 15, 5, 23, 90, 67]
ARR_LENGTH = len(arr)

# Given an array we need to find a peak element
# Peak element is the element which is higher than both its left and right neighbour
# If a peak element is present at both corner, we can check it by
# if right element is lower (left most element), and left element is lower (right most element)
# equal value is allowed at neighbour position
# start at index 1 and iterate till end, if any element satisfy peak condition we return

def basic_peak_search(array, arr_len):
    '''This function does a linear search checking each element'''
    peak = ""
    if arr_len == 0:
        return array[0]

    if array[0] > array[1]:
        peak = array[0]
    elif array[arr_len-1] > array[arr_len-2]:
        peak = array[arr_len-1]

    for i in range(1, arr_len - 1):
        if array[i-1] <= array[i] >= array[i+1]:
            peak = array[i]

    return peak

# Efficient Approach
# There will always be peak element, there will always be higher or equal
# element present at any position.

def binary_peak_search(array, arr_len):
    '''This function is similar to binary search but using unsorted array'''
    low = 0
    high = arr_len - 1

    while low <= high:
        mid = (low + high) // 2
        # Checks for peak at corner positions
        if (mid == 0 or array[mid] >= array[mid - 1]) and\
              (mid == arr_len-1 or array[mid] >= array[mid + 1]):
            return mid

        # Checks for peak at remaining positions
        if mid > 0 and array[mid] <= array[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
