array = [[5, 10], [2, 3], [6, 8], [1, 7], [1, 10], [2, 3]]


def merge_overlapping(arr):
    """Checks for any overlap within elements and merge them if true"""
    # Sort Array in place
    arr.sort(key=lambda ele: ele[0])
    res = 0

    # Changes are made in-place
    for i in range(1, len(arr)):
        # Since after sorting first element of every element is in order
        # We will just check if second value is less than res
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1], arr[i][1])
        # If second value is more than res, make current element the new merge res
        else:
            res += 1
            arr[res] = arr[i]

    # Prints the result
    for i in range(res + 1):
        print(arr[i], end=" ")


merge_overlapping(array)
