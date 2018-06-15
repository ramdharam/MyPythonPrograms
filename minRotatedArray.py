class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return

        if len(nums) == 1:
            return nums[0]
        ## check mid
        ## 1. if mid  > r --> array rotated to the right so lowest will be on the right
        ## 2. if mid  > l -- > looks good
        ## 3. if mid <  l --> array rotated to left -- so lowest in left
        ## 4. if mid < r -- > looks good
        s = len(nums)
        l, r = 0, s - 1

        while l < r:
            mid = (l + r) / 2

            if nums[mid] < nums[mid-1] and mid > 0:
                return nums[mid]
            if nums[l] <= nums[mid] and nums[mid] > nums[r]:
                l = l+1
            else:
                r = r-1
        return nums[l]






obj = Solution()
arr = [4,5,6,7,0,1,2]
out = (obj.findMin(arr))
print out