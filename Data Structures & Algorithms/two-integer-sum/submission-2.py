"""
Understand:
Input - array of ints = nums & int target
Output - array of index that return i + j == target (values) & i != j

Plan:
- dictionary with index & value

Implement:
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums): #i = index & n = value
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return
        
            

        