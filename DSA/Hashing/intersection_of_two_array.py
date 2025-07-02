'''Intersection of Two Array'''
arr1 = [10, 15, 20, 15, 30, 30, 5]
arr2 = [30, 5, 30, 80]

def intersection(arr1, arr2, n, m):
    '''Using nested for-loop to find all the intersection points'''
    res = 0
    for i in range(n):
        flag = False
        # Checks previously visited sub-array for duplicates
        for j in range(i):
            if arr1[j] == arr1[i]:
                flag = True
                break
        
        if flag == True:
            continue
        
        # Intersection check happens here
        for j in range(m):
            if arr1[i] == arr2[j]:
                res += 1
                break
    
    return res

def two_set_intersection(arr1, arr2):
    '''Creates two sets and then compare to find two intersection'''
    set_1 = set(arr1)
    set_2 = set(arr2)

    res = 0
    for ele in set_1:
        if ele in set_2:
            res += 1
    
    return res

def one_set_intersection(arr1, arr2):
    '''Create one set and compare with the other array to find the intersection'''
    set_1 = set(arr1)

    res = 0
    for i in range(len(arr2)-1, -1, -1):
        if arr2[i] in set_1:
            res += 1
            set_1.remove(arr2[i])
    
    return res

print(intersection(arr1, arr2, len(arr1), len(arr2)))
print(two_set_intersection(arr1, arr2))
print(one_set_intersection(arr1, arr2))

# Compare two set and get the common elements in return
print(len(set(arr1) & set(arr2)))
