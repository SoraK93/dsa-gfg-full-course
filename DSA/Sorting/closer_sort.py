def closer(self, arr, n,  x):
    '''This function will sort a closer sorted array where the position of elements will deviate by a max of 1'''
    # create high low pointer
    low, high = 0, n - 1
    while low <= high:
        # get mid point and start checking for values around mid point
        mid = low + (high - low) // 2
        
        if arr[mid] == x:
            return mid
        
        if mid > low and arr[mid - 1] == x:
            return mid - 1
        
        if mid < high and arr[mid + 1] == x:
            return mid + 1
        
        # if values are not present around mid point, we will change our high/ low accordingly
        if arr[mid] > x:
            high = mid - 2
        else:
            low = mid + 2
    
    return -1