class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        s = [0] * 2
        for i, v in enumerate(nums):
            s[nums[i]] += 1
            while s[0] > 1:
                s[nums[left]] -= 1
                left += 1
            ans = max(ans, i - left)
        return ans