class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevNums = {}

        for i, n in enumerate(nums):
            if n in prevNums:
                return True
            prevNums[n] = i
        return False