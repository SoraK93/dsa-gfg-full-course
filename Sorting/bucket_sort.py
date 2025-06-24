'''Bucket Sort = It is mainly useful when input is uniformly distributed over a range.
A simple way is to aplly acomparison based sorting algorithm, but we cannot use counting sort here since the keys are floating point numbers.
And as counting sort require keys as index, it won't be viable here.

Insertion sort is more prefered here, compared to .sort()

Index calculation when our bucket sort range starts at min_value
bucket_index = (element - min_value) * num_buckets // (max_value - min_value + 1)
'''
arr = [30, 40, 10, 80, 5, 12, 70]
k = 4

def bucket_sort(arr, k):
    '''This function is creating k no. of buckets and using sort() to sort through all those buckets and merge them, resulting in a sorted array'''
    # get max range of our bucket
    max_value = max(arr) + 1
    # create nested array containing k no. of empty arrays
    bucket = [[] for _ in range(k)]

    # the code is sloting all the elements based on the calculated index
    # After this loop every element of the array will be in its range appropriate slot/bucket
    for ele in arr:
        index = (ele * k) // max_value
        bucket[index].append(ele)
    
    # by using .sort() we are sorting all the nested buckets individually
    for slot in bucket:
        slot.sort()
    
    # clear the original array and push each of the nested buckets in to the original array
    # this step creates the complete sorted array
    arr.clear()
    for slot in bucket:
        arr.extend(slot)

bucket_sort(arr, k)
print(arr)
