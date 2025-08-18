class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_save = left = 0
        for i, val in enumerate(nums):
            while nums[left] * k < val:
                left += 1
            max_save = max(max_save, i - left + 1)
        return len(nums) - max_save