array = [2, 3, 4, 8, 9, 20, 40]
x = 62

# Naive Approach
def naive_triplet(arr, value):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i]+arr[j]+arr[k] == value:
                    return True
    return False

# Efficient Approach
# Use Pair Sum Problem as a sub-routine
def efficient_triplet(arr, value):
    n = len(arr)
    for i in range(n):
        print(arr[i])
        return arr[i] + isPairSum(arr[i:n], value - arr[i]) == value

def isPairSum(arr, value):
    low = 0
    high = len(arr) - 1
    while low < high:
        calc = arr[low] + arr[high]
        if calc == value:
            return calc
        elif calc > value:
            high -= 1
        else:
            low += 1
    return 0

print(efficient_triplet(array, x))