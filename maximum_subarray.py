class Solution:
    def maxSubArray(self, nums) -> int:
        maxsum = nums[0]
        cur = 0
        for n in nums:
            cur = max(n, cur + n)
            maxsum = max(maxsum, cur)
        return maxsum
