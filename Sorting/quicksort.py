def quick_sort(arr, low, high):
    if low < high:
        partition = partition_index(arr, low, high)
        quick_sort(arr, low, partition-1)
        quick_sort(arr, partition+1, high)

def partition_index(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    print(arr)
    
    arr[low], arr[right] = arr[right], arr[low]
    return right


if __name__ == "__main__":
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    quick_sort(A, 0, len(A)-1)
    print(A)