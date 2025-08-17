class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        tmpans, ans = 0, 0

        for i, val in enumerate(s):
            if val in 'aeiou':
                tmpans += 1
            ans = max(ans, tmpans)
            if i < k - 1:
                continue
            if s[i - k + 1] in 'aeiou':
                tmpans -= 1
        
        return ans