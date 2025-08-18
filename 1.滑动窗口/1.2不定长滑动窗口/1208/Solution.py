class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        left = 0
        tmpsum = 0
        for i, val in enumerate(s):
            tmpsum += abs(ord(s[i]) - ord(t[i]))
            while tmpsum > maxCost:
                tmpsum -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, i - left + 1)
        return ans
