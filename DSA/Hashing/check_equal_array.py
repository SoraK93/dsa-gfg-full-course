from collections import Counter


class Solution:
    # Function to check if two arrays are equal or not.

    @staticmethod
    def check_equal(a, b) -> bool:
        count = Counter(a)
        for num in b:
            if num in count:
                count[num] -= 1
                if not count[num]:
                    count.pop(num)
            else:
                return False
        return True


array1 = [1, 2, 5, 4, 0]
array2 = [2, 4, 5, 0, 1]
check_equal = Solution.check_equal(array1, array2)
print(check_equal)
