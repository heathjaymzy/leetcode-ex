class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for i, v in enumerate(s):
            while cnt[v] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
# Set用法
def Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = set()
        left = 0
        for i, v in enumerate(s):
            while c in cnt:
                cnt.remove(s[left])
                left += 1
            cnt.add(c)
            ans = max(ans, i - left + 1)
        return ans