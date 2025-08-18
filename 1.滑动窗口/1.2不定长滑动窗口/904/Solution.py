class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        bows = defaultdict(int)
        left = 0
        ans = 0
        for i, val in enumerate(fruits):
            bows[val] += 1
            while len(bows) > 2:
                bows[fruits[left]] -= 1
                if bows[fruits[left]] == 0:
                    del(bows[fruits[left]])
                left += 1
            ans = max(ans, i - left + 1)
        return ans