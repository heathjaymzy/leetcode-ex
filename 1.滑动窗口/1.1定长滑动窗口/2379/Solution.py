class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = inf
        tmpans = 0
        for i, val in enumerate(blocks):
            # 1. 白色个数 = 操作次数
            if val is 'W':
                tmpans += 1
            if i < k - 1:
                continue
            ans = min(tmpans, ans)
            if blocks[i - k + 1] is 'W':
                tmpans -= 1
        return ans
