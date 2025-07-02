'''Two Pointer Approach using Sorted Array'''
arr = [2, 4, 8, 9, 11, 12, 20, 30]
VALUE = 20

# Basic Approach
def basic_two_pointer(array, total):
    '''This function uses linear search to find the required sum'''
    arr_length = len(array)
    for i in range(arr_length - 1):
        for j in range(i + 1, arr_length):
            if array[i] + array[j] == total:
                return True
    return False
print(basic_two_pointer(arr, VALUE))

# Efficient Approach
def efficient_two_pointer(array, total):
    '''This function uses pointer method to check if sum is available in the array'''
    low = 0
    high = len(array) - 1
    while low < high:
        calc = array[low] + array[high]
        if calc == total:
            print(array[low], array[high])
            return True
        elif calc > total:
            high -= 1
        else:
            low += 1
    return False
print(efficient_two_pointer(arr, VALUE))
