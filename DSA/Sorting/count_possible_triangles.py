arr = [10, 21, 22, 100, 101, 200, 300]

def countTriangles(self, arr):
    # sorting array will make finding triangle related inequality much easier
    count = 0
    arr.sort()
    
    for i in range(2, len(arr)):
        # using pointers to get two sides of the triangle
        left, right = 0, i - 1
        
        while left < right:
            if arr[left] + arr[right] > arr[i]:
                # decrement right since our current set can form a triangle
                count += right - left
                right -= 1
            else:
                left += 1
                
    return count