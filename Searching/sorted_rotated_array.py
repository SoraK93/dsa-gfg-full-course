'''Search in a Sorted Rotated Array'''
sorted_array = [10, 20, 30, 40, 50, 8, 9]
X = 30

# We are given a possible sorted rotated array and lookup value
# Or we can compare first and last element to find if there is a rotation
# check of first element is higher or lower than lookup value
# if its higher,
# we will run a reverse loop and start from end till we find match or
# element which is lower than lookup value
# else, do similar expression but using a normal loop

def basic_search(arr, lookup_value):
    '''This function is a simple loop searching for lookup value'''
    for i, value in enumerate(arr):
        if value == lookup_value:
            return i
    return -1

print("Basic Search: ", basic_search(sorted_array, X))

# Binary Search Function
# Since we are doing binary search, we will need the mid value (start + end // 2).
# compare both corner to check which side is sorted.
# if start < mid (then left sorted), if mid < end (then right sorted)

def binary_search(arr, length, value):
    '''This function does a binary search on a sorted array, checking of any rotation if present.
    And looking up \'value\' in the array'''
    low = 0
    high = length - 1
    while low < high:
        mid = (low + high) // 2
        # If value is equal to mid value
        if arr[mid] == value:
            return mid
        # Left side of the array is sorted
        if arr[low] < arr[mid]:
            # Checks if value is inside the left range
            if arr[low] <= value < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right side of the array is sorted
        else:
            # Checks if value is inside the right range
            if arr[mid] < value <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
