class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        tmpans = 0
        for i, val in enumerate(arr):
            tmpans += val
            if i < k - 1:
                continue
            if tmpans >= threshold * k:
                cnt += 1
            tmpans -= arr[i - k + 1]
        return cnt