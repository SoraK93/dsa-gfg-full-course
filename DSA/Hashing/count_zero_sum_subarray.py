"""Count Zero Sum Sub arrays"""
# You are given an array arr[] of integers. Find the total count of sub arrays with their sum equal to 0.


def pos_subarray_sum_hash(arr, value):
    """Using hash object and loop to get through the array and
    simultaneously identify sub-arrays for all possible zero-sum"""
    hash_map = {}
    curr_sum = 0
    output = []

    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == value:
            output.append((value, i))

        # Stores current index and later added to hash_map as index of current pre-sum
        index_of_pre_sum = []
        if curr_sum in hash_map:
            # Since a zero-sum is found, we can use pre_sum index and current index to get our sub-array range
            index_of_pre_sum = hash_map.get(curr_sum)
            for idx in index_of_pre_sum:
                output.append((idx+1, i))

        index_of_pre_sum.append(i)
        hash_map[curr_sum] = index_of_pre_sum

    return output


def count_subarray_sum_hash(arr):
    """Using dict() we are incrementing occurrence count of pre-sum key and
    adding it to output whenever pre-sum repeats"""
    count = {0: 1}
    pre_sum = 0
    output = 0

    for i in range(len(arr)):
        pre_sum += arr[i]
        output += count.get(pre_sum, 0)
        count[pre_sum] = count.get(pre_sum, 0) + 1

    return output


array = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
total = 0
print(pos_subarray_sum_hash(array, total))
print(count_subarray_sum_hash(array))
