class Solution:
    #User function Template for python3
    #Function to merge three sorted arrays into a single array.
    def mergeThree(self, A,B,C):
        #code here
        temp_a_to_b = self.mergeTemp(A, B)
        temp_b_to_c = self.mergeTemp(temp_a_to_b, C)
        return temp_b_to_c
        
    def mergeTemp(self, arr1, arr2):
        temp = []
        i, j = 0, 0
        n, m = len(arr1), len(arr2)
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                temp.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                temp.append(arr2[j])
                j += 1
            else:
                temp.extend([arr1[i], arr2[j]])
                i += 1
                j += 1
        
        if i != n:
            temp += arr1[i:]
        else:
            temp += arr2[j:]
        
        return temp
    
A = [1, 2, 3, 4] 
B = [1, 2, 3, 4, 5] 
C = [1, 2, 3, 4, 5, 6]

print(Solution().mergeThree(A,B,C))
