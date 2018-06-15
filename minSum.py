class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        start, end = 0, 0
        l = len(nums)
        tot = (2 ** 31)
        sum = nums[start]
        while start < len(nums) and end < len(nums):
            if sum >= s:
                tot = min(tot, end - start + 1)
                sum -= nums[start]
                start += 1

            elif sum < s and end != len(nums)-1:
                end += 1
                sum += nums[end]
            else:
                return tot if tot != (2 **31) else 0
        return tot if tot != (2**31) else 0


s = Solution()
print (s.minSubArrayLen(30, [1,2,3,4,7]))