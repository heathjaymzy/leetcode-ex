class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        tmpans = 0
        for i, val in enumerate(nums):
            tmpans += val
            if i < k * 2:
                continue
            avgs[i - k] = tmpans // (k * 2 + 1)
            tmpans -= nums[i - 2 * k]
        return avgs