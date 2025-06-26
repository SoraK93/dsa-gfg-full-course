'''Radix Sort - The idea of it is to do digit by digit starting from least significant digit to most significant digit.'''
arr = [319, 212, 6, 8, 100, 500]

def redix_sort(arr):
    '''This function uses redix sort with counting sort as a sub-routine'''
    # Create the initial values 
    # Largest is needed so that we can get the highest number of units present in a digit (will be using % later to calcuate that, refer index_cal())
    largest = max(arr)
    # exp represents total digits available in max(arr) (hundred digit in our current example)
    # starts by calculating unit place digits.
    exp = 1
    # Higher base values means required space increases, but speed will decrease
    # Balance this out based on our needs
    BASE = 10
    # Stops after we have sorted highest possible digit available in they array
    while largest // exp > 1:
        counting_sort(arr, exp, BASE)
        exp *= BASE

def index_calc(value, exp, base):
    '''This function calculates index value for the auxillary array used in count sort function'''
    return (value // exp) % base

def counting_sort(array, exponent, base):
    # Create two arrays output stores sorted values and count stores position of these values
    output = [0] * len(array)
    count = [0] * base

    for ele in array:
        index = index_calc(ele, exponent, base)
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i-1]

    for i in range(len(arr)-1, -1, -1):
        index = index_calc(arr[i], exponent, base)
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    arr[:] = output

redix_sort(arr)
print(arr)
print(1//2)