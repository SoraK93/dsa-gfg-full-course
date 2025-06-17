'''Count Occurrences in a Sorted Array'''
arr = [10, 20, 20, 20, 20, 20, 20, 30, 30]
SEARCH_VALUE = 80

# Linear Search
def linear_occurrences(array, value):
    '''This function iterates through an array and checks for the given value'''
    count = 0
    for ele in array:
        if ele == value:
            count += 1
        elif ele > value:
            break
    return count
print(linear_occurrences(arr, SEARCH_VALUE))

# Binary Search
def binary_occurances(array, value):
    '''This function iterates through an array using binary search algorithm'''
    low = 0
    high = len(array) - 1
    index = None
    count = 0

    # Find a array[index] which equals value
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == value:
            index = mid
            break
        if array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    # If index is none means given value was not found in the array
    if index is None:
        return count

    # Checks left side
    index_left = index - 1
    while index_left >= 0 and array[index_left] == value:
        index_left -= 1
        count += 1
    # Checks right side
    index_right = index + 1
    while index_right <= high and array[index_right] == value:
        index_right += 1
        count += 1

    return count + 1

print(binary_occurances(arr, SEARCH_VALUE))
