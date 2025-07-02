'''Median of Two Sorted Arrays'''
array1 = [1,15,12,26,38]
array2 = [2,30,13,17,45]

# Naive Approach
def concat_calc_median(arr1, arr2):
    '''This function concatenate two array then sort and find median'''
    array = arr1 + arr2
    array.sort()
    n = len(array)
    median_index = n // 2
    if n % 2:
        print(median_index)
        return array[median_index]
    else:
        return (array[median_index] + array[median_index-1]) / 2

print(concat_calc_median(array1, array2))

# Efficient Approach
def binary_calc_median(arr1, arr2):
    # Makes sure arr1 is smaller array
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    n, m = len(arr1), len(arr2)
    low, high = 0, n

    while low <= high:
        # arr1 & arr2 contributes this many elements towards left partition
        i1 = (low + high) // 2
        i2 = (n + m + 1) // 2 - i1

        # Covers edge cases where arr1 or arr2 falls into left partition entirely
        mnr1 = float("inf") if i1 == n else arr1[i1]
        mxl1 = float("-inf") if i1 == 0 else arr1[i1-1]
        mnr2 = float("inf") if i2 == m else arr2[i2]
        mxl2 = float("-inf") if i2 == 0 else arr2[i2-1]

        # Visually, the above four statement will look like this in an array
        # [mxl1, mxl2, mnr1, mnr2]

        # Compares selected left and right subarray element of both array
        # max of set1 (arr1) <= min of set2 (arr2) && max of set1 (arr2) <= min of set2 (arr1)
        if mxl1 <= mnr2 and mxl2 <= mnr1:
            # If true, check combined array length (even/odd) and return median
            if (n+m) % 2 == 0:
                print("Even length")
                return (max(mxl1, mxl2) + min(mnr1, mnr2)) / 2
            else:
                return max(mxl1, mxl2)
        # Reduce end point of arr1 (high) until above condition becomes true
        elif mxl1 > mnr2: # max of set1 (arr1) > min of set2 (arr2)
            high -= 1
        else: # max of set1 (arr2) > min of set2 (arr1)
            low += 1

print(binary_calc_median(array1, array2))
