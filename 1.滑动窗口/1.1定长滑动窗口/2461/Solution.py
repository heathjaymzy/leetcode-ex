class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        tmpans = 0
        for i, val in enumerate(nums):
            tmpans += val
            cnt[nums[i]] += 1
            if i < k - 1:
                continue
            if len(cnt) == k:
                ans = max(ans, tmpans)
            # 处理出
            tmpans -= nums[i - k + 1]
            cnt[nums[i - k + 1]] -= 1
            if cnt[nums[i - k + 1]] == 0:
                del(cnt[nums[i - k + 1]])
            
        return ans