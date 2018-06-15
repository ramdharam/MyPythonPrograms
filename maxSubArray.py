def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    currSum, maxSum = nums[0], nums[0]
    for i in xrange(1, len(nums)):
        currSum = max(currSum + nums[i], nums[i])
        maxSum = max(maxSum, currSum)
    return maxSum


a= [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(a))