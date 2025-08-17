class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = tmpans = 0
        cnt = defaultdict(int)
        for i, val in enumerate(nums):
            # 1. 入窗口
            tmpans += val
            # 1.1 更新hash表，用于计数
            cnt[nums[i]] += 1
            # 2. 初始化窗口
            if i < k - 1:
                continue
            # 3. 更新ans
            if len(cnt) >= m:
                ans = max(ans, tmpans)
            # 4. 出表
            tmpans -= nums[i - k + 1]
            # 4.1 更新hash表计数
            cnt[nums[i - k + 1]] -= 1
            if cnt[nums[i - k + 1]] == 0:
                # 4.2 处理hash表中值==0的部分
                del cnt[nums[i - k + 1]]
        return ans