def merge_sort(A):
    # Base case: Array cannot be lower than 2 elements.
    if len(A) > 1:
        # Get mid index
        mid = len(A) // 2

        # Creating subarrays
        left = A[:mid]
        right = A[mid:]

        # Recursively call merge_sort on both subarray, until we reach the atomic level
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        # Sort array until left / right is completely sorted
        while len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        
        # Sort the remaining arrays, will execute either one of these while loops
        while len(left) > i:
            A[k] = left[i]
            k += 1
            i += 1
        
        while len(right) > j:
            A[k] = right[j]
            k += 1
            j += 1


if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    merge_sort(A)
    print(A)