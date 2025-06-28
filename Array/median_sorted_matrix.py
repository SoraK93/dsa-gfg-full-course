from bisect import bisect
from typing import List
import heapq

# Binary Search Algorithm Approach
def getMed(mat):
    row, col = len(mat), len(mat[0])
    min_value, max_value = mat[0][0], mat[0][col - 1]
    
    for i in range(1, row):
        min_value = min(min_value, mat[i][0])
        max_value = max(max_value, mat[i][col - 1])
    
    # Index position of median in a normal sorted array
    target_pos = (row * col + 1) // 2

    while min_value < max_value:
        mid = (min_value + max_value) // 2
        
        mid_pos = 0
        for i in range(row):
            mid_pos += bisect(mat[i], mid)
        
        if mid_pos < target_pos:
            min_value = mid + 1
        else:
            max_value = mid
    
    return min_value

array = [[5, 11, 40],[1, 2, 3],[12, 13, 15]]
print(getMed(array))

# Using a min heap - Priority Queue
class Node:
	def __init__(self, data: int, row: int, col: int):
		self.data = data
		self.row = row
		self.col = col
	def __lt__(self, other):
		return self.data < other.data

# Solution class contains the main logic to find median
class Solution:
	def median(self, matrix, R, C):
		minheap = []
		count = 0
		median = -1
		medianindex = (R * C) // 2

		for i in range(R):
			temp = Node(matrix[i][0], i, 0)
			heapq.heappush(minheap, temp)

		while count <= medianindex:
			top = heapq.heappop(minheap)
			row = top.row
			col = top.col
			median = top.data

			count += 1
			if col + 1 < C:
				col += 1
				temp = Node(matrix[row][col], row, col)
				heapq.heappush(minheap, temp)

		return median

r = 3
c = 3
matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
obj = Solution()
print(obj.median(matrix, r, c))