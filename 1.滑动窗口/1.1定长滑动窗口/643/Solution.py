class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmpans = 0
        ans = -inf
        for i, val in enumerate(nums):
            tmpans += val
            if i < k - 1:
                continue
            ans = max(tmpans, ans)
            tmpans -= nums[i - k + 1]
        return ans / k