'''
Cycle Sort
- Does minimum memory writes and can be useful for cases where memory write is costly.
Useful to solve questions like fund minimum swaps required to sort an array.
'''

arr = [20, 40, 50, 10, 30, 20]

def cycle_sort(arr):
    '''This function uses cycle sort where our number of swaps made while sorting is mostly equal to the size of array'''
    # Outer loop is skipping the last element, since our nested for-loop is comparing curr with curr+1
    for cs in range(len(arr)-1):
        # Current value and index is stored
        item = arr[cs]
        pos = cs
        # Compare current value and if satisfied increment pos, pos acts like a index value
        for i in range(cs+1, len(arr)):
            if item > arr[i]:
                pos += 1
        # Means our current value is stored at the right index
        if pos == cs:
            continue
        # Swaps current value to its correct index and update our stored value
        arr[pos], item = item, arr[pos]
        while pos != cs:
            # Reset pos value and calculate new index for the updated current value
            pos = cs
            for i in range(cs+1, len(arr)):
                if item > arr[i]:
                    pos += 1
            # This takes care of the edge case when we reach the starting pos value again after multiple swaps
            # Instead of just continue we are swaping. This makes sure we swap in the current value
            if pos == cs:
                arr[pos], item = item, arr[pos]
                continue
            arr[pos], item = item, arr[pos]


cycle_sort(arr)
print(arr)