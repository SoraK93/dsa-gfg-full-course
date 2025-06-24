'''
Counting Sort Algorithm

- Counting Sort makes few assumptions about data like being real number, between certain range
- Not a comparison based algorithm like other sorting algorithm
- Uses temp array 
'''

# Works only with simple array
arr = [1, 4, 4, 1, 0, 1]
k = 5

# Naive Approach
def counting_sort(arr, k):
    count = [0] * k
    for ele in arr:
        count[ele] += 1
    
    index = 0
    for i in range(k):
        for _ in range(count[i]):
            arr[index] = i
            index += 1

counting_sort(arr, k)    
print(arr)

# Efficient Approach
def counting_sort2(arr, k):
    # output takes all the sorted values from the array by using count to find out the indexes of those values
    output = [0] * len(arr)
    count = [0] * k

    # Counting each element and storing them as index
    for ele in arr:
        count[ele] += 1
    
    # We are getting the positions for all the values using pre-fix sum 
    for i in range(1, k):
        count[i] += count[i-1]

    # Reversing the array for stability reasons
    # will not result in overridding values, we already sorted
    for i in reversed(arr):
        # decreasing by 1 due to zero-indexing
        output[count[i]-1] = i
        # Decrementing count updates position, if its accessed later
        count[i] -= 1
    
    # overrides new output array on top of the original array
    arr[:] = output

counting_sort2(arr, k)
print(arr)

