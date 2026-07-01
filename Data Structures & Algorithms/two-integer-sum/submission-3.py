class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            toSum = target - num
            if toSum in sums:
                return [sums[toSum], i]
            sums[num] = i