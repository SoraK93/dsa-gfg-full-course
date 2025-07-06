"""Longest Consecutive Subsequence"""
# We need to find the longest subsequence in the form of [x, x+1, x+2, ..., x+i]
# with these elements appearing in any order


def longest_subsequence_naive(arr):
    """Uses sorted() to sort the array, later traverse through the array to """
    # Reduces random search in-order to find consecutive array
    sorted_arr = sorted(arr)
    # There will always be the element itself which makes up the initial consecutive count
    result, curr_sum = 1, 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i - 1] + 1 == sorted_arr[i]:
            curr_sum += 1
        else:
            curr_sum = 1
        result = max(result, curr_sum)
    return result


def longest_subsequence_hash(arr):
    hash_map = set(arr)
    result, curr_sum = 1, 1
    for i in range(len(arr)):
        # We skip all consecutive elements because all those elements have already been visited during while loop
        if arr[i] - 1 not in hash_map:
            # while loop is always run on elements that have not been visited before
            curr_sum = 1
            while arr[i] + curr_sum in hash_map:
                curr_sum += 1
            result = max(result, curr_sum)
    return result


array = [1, 9, 3, 4, 2, 20]
print(longest_subsequence_naive(array))
print(longest_subsequence_hash(array))
