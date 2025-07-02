arr1 = [15, 20, 5, 15]
arr2 = [15, 15, 15, 20, 10]

def loop_union(arr1, arr2, n, m):
    res = 0
    union = [0] * (n+m)
    for i in range(n):
        union[i] = arr1[i]
    for i in range(m):
        union[i+n] = arr2[i]
    
    for i in range(n+m):
        flag = False
        for j in range(i):
            if union[i] == union[j]:
                flag = True
                break
        
        if flag == False:
            res += 1

    return res

def two_pointer_union(arr1, arr2, n, m):
    result = []
    left, right = 0, 0

    while left < n and right < m:
        to_append = arr1[left] if arr1[left] < arr2[right] else arr2[right]
        if not result or result[-1] != to_append:
            result.append(to_append)

        if arr1[left] < arr2[right]:
            left += 1
        else:
            right += 1

    for rem in (arr1[left:], arr2[right:]):
        for ele in rem:
            if not result and result[-1] != ele:
                result.append(ele)
    
    return len(result)
    


def two_set_union(arr1, arr2):
    union = set(arr1)
    union.update(arr2)
    return len(union)
        
print(loop_union(arr1, arr2, len(arr1), len(arr2)))
print(two_set_union(arr1, arr2))
arr1.sort()
arr2.sort()
print(two_pointer_union(arr1, arr2, len(arr1), len(arr2)))